while True:
    print('+==============================================+')
    print('|      HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS  |')
    print('+==============================================+')
    print('| 1. Nhập dữ liệu đơn hàng và báo cáo thống kê |')
    print('| 2. Chuẩn hóa mã đơn hàng                     |')
    print('| 3. Ẩn số điện thoại khách hàng               |')
    print('| 4. Tìm kiếm và thay thế từ khóa trong ghi chú|')
    print('| 5. Thoát chương trình                        |')
    print('+==============================================+')

    choice = input("Mời bạn chọn chức năng (1-5): ")

    # Bẫy 6
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    # Bẫy 5
    if int(choice) not in range(1, 6):
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    if choice == "1":

        sender_name = input("Nhập tên người gửi: ")
        if not sender_name.strip():
            print("Tên người gửi không được bỏ trống")
            continue

        sender_phone = input("Nhập số điện thoại người gửi: ")
        if not sender_phone.strip():
            print("Số điện thoại người gửi không được bỏ trống")
            continue

        pickup_address = input("Nhập địa chỉ lấy hàng: ")
        if not pickup_address.strip():
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue

        receiver_name = input("Nhập tên người nhận: ")
        if not receiver_name.strip():
            print("Tên người nhận không được bỏ trống")
            continue

        receiver_phone = input("Nhập số điện thoại người nhận: ")
        if not receiver_phone.strip():
            print("Số điện thoại người nhận không được bỏ trống")
            continue

        delivery_address = input("Nhập địa chỉ giao hàng: ")
        if not delivery_address.strip():
            print("Địa chỉ giao hàng không được bỏ trống")
            continue

        order_code = input("Nhập mã đơn hàng: ")
        if not order_code.strip():
            print("Mã đơn hàng không được bỏ trống")
            continue

        delivery_note = input("Nhập ghi chú giao hàng: ")
        if not delivery_note.strip():
            print("Ghi chú giao hàng không được bỏ trống")
            continue

        processed_note = delivery_note.strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print(
            f"Tên người gửi: {sender_name.strip().title()}"
        )

        print(
            f"Tên người nhận: {receiver_name.strip().title()}"
        )

        print(
            f"Địa chỉ lấy hàng: {' '.join(pickup_address.split())}"
        )

        print(
            f"Địa chỉ giao hàng: {' '.join(delivery_address.split())}"
        )

        print(
            f"Ghi chú giao hàng: {processed_note}"
        )

        print(
            f"Độ dài ghi chú: {len(processed_note)}"
        )

        print(
            f"Số lượng từ trong ghi chú: {len(processed_note.split())}"
        )

        print(
            f"Ghi chú dạng chữ thường: {processed_note.lower()}"
        )

        print(
            f"Ghi chú dạng chữ hoa: {processed_note.upper()}"
        )

    elif choice == "2":

        if not order_code:
            print("Vui lòng nhập thông tin đơn hàng trước (chức năng 1).")
            continue

        original_code = order_code

        formatted_code = order_code.strip().upper()

        formatted_code = formatted_code.replace(" ", "-")

        if not formatted_code.startswith("GRAB-"):
            formatted_code = "GRAB-" + formatted_code

        print("\n===== CHUẨN HÓA MÃ ĐƠN HÀNG =====")
        print(f"Mã đơn hàng ban đầu: {original_code}")
        print(f"Mã đơn hàng sau chuẩn hóa: {formatted_code}")

    elif choice == "3":

        if not sender_phone or not receiver_phone:
            print("Vui lòng nhập thông tin đơn hàng trước (chức năng 1).")
            continue

        valid = True

        # Bẫy 2
        if not sender_phone.isdigit():
            print("Số điện thoại người gửi không hợp lệ")
            valid = False

        if not receiver_phone.isdigit():
            print("Số điện thoại người nhận không hợp lệ")
            valid = False

        # Bẫy 3
        if len(sender_phone) != 10:
            print("Số điện thoại người gửi không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            valid = False

        if len(receiver_phone) != 10:
            print("Số điện thoại người nhận không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            valid = False

        if valid:

            hidden_sender = (
                sender_phone[:3]
                + "*" * 5
                + sender_phone[-2:]
            )

            hidden_receiver = (
                receiver_phone[:3]
                + "*" * 5
                + receiver_phone[-2:]
            )

            print("\n===== THÔNG TIN ĐÃ ẨN =====")
            print(f"SĐT người gửi: {hidden_sender}")
            print(f"SĐT người nhận: {hidden_receiver}")

    elif choice == "4":

        # Bẫy 4
        if not delivery_note.strip():
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        keyword_search = input("Nhập từ khóa cần tìm: ")
        keyword_replace = input("Nhập từ khóa thay thế: ")

        if keyword_search in delivery_note:

            count = delivery_note.count(keyword_search)

            new_note = delivery_note.replace(
                keyword_search,
                keyword_replace
            )

            print(
                f"Số lần xuất hiện của từ khóa: {count}"
            )

            print(
                "Ghi chú giao hàng sau khi thay thế:"
            )

            print(new_note)

        else:
            print(
                "Không tìm thấy từ khóa trong ghi chú giao hàng."
            )

    elif choice == "5":
        print("Thoát chương trình")
        break