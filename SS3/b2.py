print ("- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT -- ")

# Vòng Lặp chạy đúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print ("- Đang xử lý nhân viên số", employee_number, " --- ")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input ("Nhập số ngày công trong tháng: "))

    # Kiểm tra diều kiện
    if working_days == 0:
        print ("CẢNH BÁO: Nhân viên nghi cả tháng. Không xét duyệt thưong.")
        continue

    bonus_amount = working_days * 200000
    print("-> Đã gửi Email: Chúc mừng nhận dược", bonus_amount, "VNĐ tiền thường!")
    print("------------------------------------------\n")


print ("Đã hoàn tất quá trình duyệt thưong cho 3 nhân viên!")

