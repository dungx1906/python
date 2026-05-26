print ("- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG --- ")

# Khởi tạo chiếc hộp dựng tổng tiền
total_budget = 0

# Vòng Lap chạy 3 Lần dể nhập Lương cho 3 nhân viên
for employee_number in range(1, 4):

    print ("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương
    salary = int (input (" Nhập mức lương (VNĐ) : ") )

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print ("-> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẤN BỊ LÀ:", total_budget, "VNĐ")