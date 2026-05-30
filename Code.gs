/**
 * HƯỚNG DẪN SỬ DỤNG:
 * 1. Mở file Google Sheets chứa dữ liệu của AppSheet (bảng KhachHang và HoSoThanhToan).
 * 2. Trên thanh menu, chọn Tiện ích mở rộng (Extensions) -> Apps Script.
 * 3. Xóa hết code cũ và dán toàn bộ đoạn code dưới đây vào.
 * 4. Nhấn nút Triển khai (Deploy) -> Tùy chọn triển khai mới (New deployment).
 * 5. Chọn Loại: Ứng dụng Web (Web app).
 * 6. Ai có quyền truy cập: Chọn "Bất kỳ ai" (Anyone).
 * 7. Nhấn Triển khai và copy đường link URL (Web App URL) cấp cho ứng dụng của chúng ta.
 */

function doPost(e) {
  var body = {};
  try { 
    body = JSON.parse(e.postData.contents); 
  } catch(err) {}
  
  var action = body.action || (e.parameter && e.parameter.action);
  var idHoSo = body.id || (e.parameter && e.parameter.id);
  
  if (!idHoSo || !action) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error", message: "Thiếu tham số ID hoặc action."
    })).setMimeType(ContentService.MimeType.JSON);
  }

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheetHoSo = ss.getSheetByName("HoSoThanhToan");
    
    if (action === 'delete') {
      var rowIndex = getRowIndexById(sheetHoSo, idHoSo);
      if (rowIndex > -1) {
        sheetHoSo.deleteRow(rowIndex);
        return ContentService.createTextOutput(JSON.stringify({
          status: "success", data: { id: idHoSo, deleted: true }
        })).setMimeType(ContentService.MimeType.JSON);
      }
      throw new Error("Không tìm thấy dòng để xóa");
    }
    
    if (action === 'update') {
      var rowIndex = getRowIndexById(sheetHoSo, idHoSo);
      if (rowIndex > -1) {
        var data = body.data || {};
        var headers = sheetHoSo.getDataRange().getValues()[0];
        var currentRow = sheetHoSo.getRange(rowIndex, 1, 1, headers.length).getValues()[0];
        
        for (var i = 0; i < headers.length; i++) {
          var colName = headers[i];
          if (data[colName] !== undefined && colName !== "ID_HoSo") {
             currentRow[i] = data[colName];
          }
        }
        
        sheetHoSo.getRange(rowIndex, 1, 1, headers.length).setValues([currentRow]);
        
        var updatedObj = {};
        for (var i = 0; i < headers.length; i++) {
          updatedObj[headers[i]] = currentRow[i];
        }
        
        return ContentService.createTextOutput(JSON.stringify({
          status: "success", data: updatedObj
        })).setMimeType(ContentService.MimeType.JSON);
      }
      throw new Error("Không tìm thấy dòng để cập nhật");
    }
    
    throw new Error("Action không hợp lệ cho POST.");
  } catch(error) {
     return ContentService.createTextOutput(JSON.stringify({
      status: "error", message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  var action = e.parameter.action;
  var idHoSo = e.parameter.id;
  
  if (!idHoSo && action !== 'list') {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: "Thiếu tham số ID hồ sơ hoặc action."
    })).setMimeType(ContentService.MimeType.JSON);
  }

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    
    // Lấy Sheet Hồ sơ (Thay tên "HoSoThanhToan" bằng tên Sheet thực tế của bạn)
    var sheetHoSo = ss.getSheetByName("HoSoThanhToan");
    // Lấy Sheet Khách hàng (Thay tên "KhachHang" bằng tên Sheet thực tế của bạn)
    var sheetKhachHang = ss.getSheetByName("KhachHang");
    
    if (!sheetHoSo || !sheetKhachHang) {
      throw new Error("Không tìm thấy Sheet HoSoThanhToan hoặc KhachHang.");
    }

    if (action === 'list') {
      var allHoSo = getAllData(sheetHoSo);
      // Gộp thêm thông tin KhachHang cơ bản vào danh sách nếu cần, hoặc trả về luôn
      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        data: allHoSo
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // Tìm dữ liệu Hồ sơ chi tiết
    var dataHoSo = getRowDataById(sheetHoSo, idHoSo);
    if (!dataHoSo) {
      throw new Error("Không tìm thấy Hồ sơ với ID: " + idHoSo);
    }

    // Lấy ID Khách hàng từ Hồ sơ để tìm trong bảng Khách Hàng
    var idKhachHang = dataHoSo["ID_KhachHang"] || dataHoSo["Mã KH"]; // Dự phòng tên cột
    if (idKhachHang) {
      var dataKhachHang = getRowDataById(sheetKhachHang, idKhachHang);
      // Gộp thông tin khách hàng vào object hồ sơ
      dataHoSo["KhachHang"] = dataKhachHang || {};
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      data: dataHoSo
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// Hàm phụ trợ lấy dữ liệu 1 dòng thành Object dạng JSON dựa trên cột đầu tiên (ID)
function getRowDataById(sheet, id) {
  var data = sheet.getDataRange().getValues();
  var headers = data[0];
  
  for (var i = 1; i < data.length; i++) {
    // Giả sử ID nằm ở cột đầu tiên (cột A, index = 0)
    if (data[i][0] == id) {
      var rowObject = {};
      for (var j = 0; j < headers.length; j++) {
        rowObject[headers[j]] = data[i][j];
      }
      return rowObject;
    }
  }
  return null;
}

// Hàm lấy toàn bộ dữ liệu thành mảng Object
function getAllData(sheet) {
  var data = sheet.getDataRange().getValues();
  if (data.length <= 1) return []; // Chỉ có header hoặc trống
  
  var headers = data[0];
  var result = [];
  
  for (var i = 1; i < data.length; i++) {
    var rowObject = {};
    // Bỏ qua dòng trống
    if (!data[i][0]) continue;
    
    for (var j = 0; j < headers.length; j++) {
      rowObject[headers[j]] = data[i][j];
    }
    result.push(rowObject);
  }
  return result;
}

// Hàm phụ trợ lấy index dòng
function getRowIndexById(sheet, id) {
  var data = sheet.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (data[i][0] == id) {
      return i + 1;
    }
  }
  return -1;
}
