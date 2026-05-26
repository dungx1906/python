print("--- HỆ THỐNG KHAI BÁO NHÂN VIÊN MỚI ---")
is_correct = False

while not is_correct :
    number_emp = int(input("Vui lòng nhập số lượng nhân viên mới trong tháng này: "))

    if (number_emp > 0 ):
        is_correct = True
        print("[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho 8 nhân sự mới ")
    else:
        print("[LỖi] Số lượng không hợp lệ! Vui lòng nhập con số lớn hơn 0.")
