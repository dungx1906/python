raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    if choice == "1":
        print("\nDữ liệu gốc:")
        print(raw_data)

    elif choice == "2":

        employees = raw_data.split("|")

        print("\n{:<12}{:<20}{:<18}{:<10}".format(
            "ID", "HỌ TÊN", "SĐT", "PHÒNG BAN"
        ))
        print("-" * 60)

        for employee in employees:

            fields = employee.split(";")

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip().replace("-", "")
            department = fields[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(
                f"{emp_id:<12}"
                f"{name:<20}"
                f"{phone:<18}"
                f"{department:<10}"
            )

    elif choice == "3":

        search_id = input(
            "Nhập mã nhân viên cần tìm: "
        ).strip().upper()

        found = False

        employees = raw_data.split("|")

        for employee in employees:

            fields = employee.split(";")

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip().replace("-", "")
            department = fields[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            if emp_id == search_id:
                print("\nThông tin nhân viên:")
                print(f"ID: {emp_id}")
                print(f"Họ tên: {name}")
                print(f"SĐT: {phone}")
                print(f"Phòng ban: {department}")

                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == "4":
        print("Thoát chương trình")
        break