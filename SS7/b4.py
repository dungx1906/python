registration_count = int(input("Nhập số lượng phiếu đăng ký: "))

if registration_count <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")

else:

    for i in range(1, registration_count + 1):

        print(f"\nNhập phiếu đăng ký {i}:")
        registration = input()

        parts = registration.split("|")

        # Edge Case 2
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirmation_code = (
            student_code + "_" +
            course_name.upper().replace(" ", "-")
        )

        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirmation_code}")