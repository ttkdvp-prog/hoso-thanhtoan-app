const mockData = {
  "HS001": {
    "ID_HoSo": "HS001",
    "NgayTao": "15/05/2026",
    "TrangThai": "Chờ duyệt",
    "KhachHang": {
      "Tên khách hàng": "CÔNG TY TNHH CÔNG NGHỆ BẢO LONG",
      "Người đại diện": "Ông Nguyễn Văn Nam",
      "Địa chỉ": "Số 123 Đường Trần Phú, Quận Ba Đình, TP. Hà Nội",
      "Mã số thuế": "0101234567",
      "Số tài khoản": "1903123456789",
      "Tại Ngân hàng": "Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank) - Chi nhánh Hà Nội",
      "Số Điện thoại": "0987654321"
    },
    "SoHopDong": "123/2026/HĐ-VNPT",
    "NgayKyHopDong": "01/05/2026",
    "NoiDungHopDong": "Thuê cơ sở hạ tầng viễn thông",
    "GiaTriTruocThue": "100.000.000",
    "ThueSuat": "8%",
    "TienThue": "8.000.000",
    "GiaTriSauThue": "108.000.000",
    "BangChu": "Một trăm lẻ tám triệu đồng chẵn",
    "ThoiGianThucHien": "30 ngày",
    "SoBienBanGiaoNhan": "123/BBGN-VNPT",
    "NgayGiaoNhan": "25/05/2026",
    "SoThanhLy": "123/TLHĐ-VNPT",
    "NgayThanhLy": "30/05/2026",
    "SoGiayDeNghi": "123/ĐNTT-VNPT",
    "NgayDeNghi": "30/05/2026",
    "SoToTrinh": "123/TTr-VNPT",
    "NgayToTrinh": "30/05/2026",
    "NoiDungToTrinh": "Phê duyệt thanh toán chi phí thuê cơ sở hạ tầng viễn thông theo Hợp đồng số 123/2026/HĐ-VNPT",
    "HangHoa": [
      {
        "TenHangHoa": "Ổ 6ĐND dây 5mx2 10A, có bảo vệ bằng CB",
        "DonViTinh": "Cái",
        "SoLuong": 5,
        "DonGia": "200.000",
        "TienThue": "80.001",
        "ThanhTien": "1.000.000",
        "ThanhTienNum": 1000000,
        "TienThueNum": 80001
      },
      {
        "TenHangHoa": "Ống PVC D25 750N A9025",
        "DonViTinh": "Cây",
        "SoLuong": 50,
        "DonGia": "21.500",
        "TienThue": "86.000",
        "ThanhTien": "1.075.000",
        "ThanhTienNum": 1075000,
        "TienThueNum": 86000
      }
    ]
  }
};

// Hàm lấy dữ liệu từ URL ?id=...
async function fetchHoSoData() {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  
  if (!id) {
    console.warn('Không tìm thấy ID trong URL. Sử dụng dữ liệu mẫu HS001.');
    return mockData["HS001"];
  }

  // --- KẾT NỐI API THỰC TẾ ---
  // Dán đường link Web App URL của Google Apps Script vào biến này:
  const GOOGLE_SCRIPT_API_URL = "https://script.google.com/macros/s/AKfycbwzPGEp-QZJk-puwLV_Xg9Dg6CvYIIJU2K3lh-DTVJrT_z4GFrdtuyXavyXhK-q4ZB_/exec"; 
  
  if (GOOGLE_SCRIPT_API_URL !== "") {
      try {
          const response = await fetch(`${GOOGLE_SCRIPT_API_URL}?id=${id}`);
          const result = await response.json();
          if (result.status === "success") {
              return result.data;
          } else {
              alert("Lỗi từ máy chủ dữ liệu: " + result.message);
              return null;
          }
      } catch (error) {
          alert("Lỗi kết nối mạng: " + error.message);
          return null;
      }
  }

  // Nếu chưa có API, sử dụng dữ liệu giả lập (mockData)
  if (mockData[id]) {
    return mockData[id];
  } else {
    alert("Không tìm thấy dữ liệu cho ID: " + id);
    return null;
  }
}

// Hàm điền dữ liệu vào các thẻ HTML có thuộc tính data-field
function renderData(data) {
  if (!data) return;

  // Render các trường đơn lẻ
  const elements = document.querySelectorAll('[data-field]');
  elements.forEach(el => {
    const fieldPath = el.getAttribute('data-field');
    
    const keys = fieldPath.split('.');
    let value = data;
    for (const key of keys) {
      if (value && value[key] !== undefined) {
        value = value[key];
      } else {
        value = "";
        break;
      }
    }
    
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.value = value;
    } else {
        el.innerText = value;
    }
  });

  // Render danh sách (bảng) dựa trên data-list
  const listContainers = document.querySelectorAll('[data-list]');
  listContainers.forEach(tbody => {
    const listKey = tbody.getAttribute('data-list');
    const items = data[listKey];
    if (Array.isArray(items) && items.length > 0) {
      // Tìm template row
      const templateRow = tbody.querySelector('tr[data-template="true"]');
      if (templateRow) {
        const rowHtml = templateRow.outerHTML;
        tbody.innerHTML = ''; // Xóa template cũ
        let total = 0;
        let vatTotal = 0;
        
        items.forEach((item, index) => {
          let newRowHtml = rowHtml.replace('data-template="true"', '');
          // Thay thế STT
          newRowHtml = newRowHtml.replace('{STT}', index + 1);
          // Thay thế các cột {CotABC}
          for (const key in item) {
            const regex = new RegExp(`{${key}}`, 'g');
            newRowHtml = newRowHtml.replace(regex, item[key]);
          }
          tbody.insertAdjacentHTML('beforeend', newRowHtml);
          
          if(item.ThanhTienNum) total += item.ThanhTienNum;
          if(item.TienThueNum) vatTotal += item.TienThueNum;
        });

        // Điền lại tổng cộng nếu có footer
        const footerTotal = tbody.parentElement.querySelector('[data-sum="ThanhTien"]');
        if (footerTotal) footerTotal.innerText = total.toLocaleString('vi-VN');
        
        const footerVat = tbody.parentElement.querySelector('[data-sum="TienThue"]');
        if (footerVat) footerVat.innerText = vatTotal.toLocaleString('vi-VN');
        
        const footerGrand = tbody.parentElement.querySelector('[data-sum="TongTien"]');
        if (footerGrand) footerGrand.innerText = (total + vatTotal).toLocaleString('vi-VN');
      }
    }
  });
}

// Chạy khởi tạo khi trang load
document.addEventListener('DOMContentLoaded', async () => {
    // Chỉ render dữ liệu nếu có các thẻ cần điền (dành cho trang in)
    const elementsToRender = document.querySelectorAll('[data-field]');
    if (elementsToRender.length > 0) {
        const data = await fetchHoSoData();
        renderData(data);
    }
});
