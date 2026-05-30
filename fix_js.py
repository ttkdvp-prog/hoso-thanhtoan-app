import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_script = """    <script>
        // Cấu hình URL API (giống admin.html)
        const APPS_SCRIPT_URL = window.APPS_SCRIPT_URL || "https://script.google.com/macros/s/AKfycbwzPGEp-QZJk-puwLV_Xg9Dg6CvYIIJU2K3lh-DTVJrT_z4GFrdtuyXavyXhK-q4ZB_/exec";

        function docTienBangChu(SoTien) {
            if (SoTien == 0) return "Không đồng";
            var ChuSo = [" không ", " một ", " hai ", " ba ", " bốn ", " năm ", " sáu ", " bảy ", " tám ", " chín "];
            var Tien = ["", " nghìn", " triệu", " tỷ", " nghìn tỷ", " triệu tỷ"];
            function docSo3ChuSo(baso) {
                var tram, chuc, donvi, KetQua = "";
                tram = parseInt(baso / 100); chuc = parseInt((baso % 100) / 10); donvi = baso % 10;
                if (tram == 0 && chuc == 0 && donvi == 0) return "";
                if (tram != 0) { KetQua += ChuSo[tram] + " trăm "; if ((chuc == 0) && (donvi != 0)) KetQua += " linh "; }
                if ((chuc != 0) && (chuc != 1)) { KetQua += ChuSo[chuc] + " mươi"; if ((chuc == 0) && (donvi != 0)) KetQua += " linh "; }
                if (chuc == 1) KetQua += " mười ";
                switch (donvi) {
                    case 1: if ((chuc != 0) && (chuc != 1)) KetQua += " mốt "; else KetQua += ChuSo[donvi]; break;
                    case 5: if (chuc == 0) KetQua += ChuSo[donvi]; else KetQua += " lăm "; break;
                    default: if (donvi != 0) KetQua += ChuSo[donvi]; break;
                }
                return KetQua;
            }
            var lan = 0, i = 0, so = 0, KetQua = "", tmp = "", ViTri = new Array();
            if (SoTien < 0) return "Số tiền âm !";
            if (SoTien > 8999999999999999) return "Số quá lớn!";
            ViTri[5] = Math.floor(SoTien / 1000000000000000); SoTien = SoTien - parseFloat(ViTri[5].toString()) * 1000000000000000;
            ViTri[4] = Math.floor(SoTien / 1000000000000); SoTien = SoTien - parseFloat(ViTri[4].toString()) * 1000000000000;
            ViTri[3] = Math.floor(SoTien / 1000000000); SoTien = SoTien - parseFloat(ViTri[3].toString()) * 1000000000;
            ViTri[2] = parseInt(SoTien / 1000000); ViTri[1] = parseInt((SoTien % 1000000) / 1000); ViTri[0] = parseInt(SoTien % 1000);
            if (ViTri[5] > 0) lan = 5; else if (ViTri[4] > 0) lan = 4; else if (ViTri[3] > 0) lan = 3; else if (ViTri[2] > 0) lan = 2; else if (ViTri[1] > 0) lan = 1; else lan = 0;
            for (i = lan; i >= 0; i--) {
                tmp = docSo3ChuSo(ViTri[i]); KetQua += tmp;
                if (ViTri[i] > 0) KetQua += Tien[i];
                if ((i > 0) && (tmp.length > 0)) KetQua += ',';
            }
            if (KetQua.substring(KetQua.length - 1) == ',') KetQua = KetQua.substring(0, KetQua.length - 1);
            KetQua = KetQua.trim() + " đồng";
            return KetQua.charAt(0).toUpperCase() + KetQua.slice(1);
        }

        async function loadDataAndPrint() {
            const urlParams = new URLSearchParams(window.location.search);
            const id = urlParams.get('id');
            if (!id) {
                alert("Không tìm thấy ID hồ sơ trong URL (ví dụ: ?id=HS001)");
                return;
            }

            try {
                document.title = "Đang tải dữ liệu...";
                const response = await fetch(`${APPS_SCRIPT_URL}?action=get&id=${id}`);
                const result = await response.json();
                
                if (result.status === "success") {
                    const data = result.data;
                    let content = document.getElementById('contract-content').innerHTML;
                    
                    const flattenObj = (ob) => {
                        let res = {};
                        for (const i in ob) {
                            if ((typeof ob[i]) === 'object' && !Array.isArray(ob[i]) && ob[i] !== null) {
                                const temp = flattenObj(ob[i]);
                                for (const j in temp) {
                                    res[i + '.' + j] = temp[j];
                                }
                            } else {
                                res[i] = ob[i];
                            }
                        }
                        return res;
                    };
                    
                    const flatData = flattenObj(data);

                    // Tự động tính tiền bằng chữ nếu có trường giá trị
                    let giaTri = flatData['GiaTriSauThue'] || flatData['GiaTri'] || flatData['Tổng tiền'] || 0;
                    if (giaTri) {
                        const amount = Number(String(giaTri).replace(/[^0-9-]/g, ''));
                        if (!isNaN(amount) && !flatData['BangChu']) {
                            flatData['BangChu'] = docTienBangChu(amount);
                        }
                        // Format số tiền có chấm phân cách
                        if (flatData['GiaTriSauThue']) flatData['GiaTriSauThue'] = amount.toLocaleString('vi-VN');
                    }

                    // Tự động lấy dữ liệu từ AppSheet để điền vào tất cả các chỗ {...}
                    content = content.replace(/\\{([^{}]+)\\}/g, function(match, key) {
                        // Tìm kiếm linh hoạt, kể cả khi sai khác khoảng trắng
                        const cleanKey = key.trim();
                        if (flatData[cleanKey] !== undefined) return flatData[cleanKey];
                        // Tìm thử theo KhachHang.Key nếu thiếu
                        if (flatData['KhachHang.' + cleanKey] !== undefined) return flatData['KhachHang.' + cleanKey];
                        // Mặc định trả về dấu ... nếu không tìm thấy dữ liệu
                        return '.........................';
                    });

                    document.getElementById('contract-content').innerHTML = content;
                    document.title = "In Hợp Đồng - " + id;
                    
                    setTimeout(() => window.print(), 500);
                } else {
                    alert("Lỗi tải dữ liệu: " + result.message);
                }
            } catch (err) {
                alert("Không thể kết nối tới server. Vui lòng kiểm tra lại link API.");
            }
        }

        window.onload = loadDataAndPrint;
    </script>"""

# Replace the old script block
html = re.sub(r'<script>.*?</script>', new_script, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dashboard-sheets-expert/assets/dashboard-shell/vanilla/hop_dong_template.html', 'w', encoding='utf-8') as f:
    f.write(html)
