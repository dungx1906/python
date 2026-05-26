count = 0
while count < 3:
    id_imp = input("Nhập mã nhân viên: ").strip()
    name = input("Nhập họ và tên: ").strip()
    department = input("Nhập phòng ban công tác: ")
    if id_imp == "" or name == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Huỷ bỏ tạo hồ sơ cho nhân viên này")
    else:
        print(f'Mã nhân viên: {id_imp} - Họ và tên nhân viên: {name} - Phòng ban công tác: {department}')
        count = count + 1
