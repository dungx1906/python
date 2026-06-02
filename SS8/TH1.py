while True:
    print('+====================================+')
    print('|  Hệ thống quản lí nội dung tiktok  |')
    print('+====================================+')
    print('1. Nhập và phân tích thông tin video |')
    print('2. Chuẩn hóa tên tài khoản           |')
    print('3. Kiểm tra tính hợp lệ của hashatg  |')
    print('4. Tìm kiếm và thay thế từ khóa trong mô tả |')
    print('5. Thoát chương trình                |')
    print('+====================================+')

    choice = input('Mời bạn chọn chức năng (1-5):')

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    if int(choice) not in range(1, 6):
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    if choice == "1":
        user_name = input("Nhập tên tài khoản người dùng: ")
        if not user_name.strip():
            print("Tên tài khoản không được bỏ trống")
            continue

        title_video = input("Nhập tiêu đề video: ")

        describe_video = input("Nhập mô tả video: ")
        if not user_name.strip():
            print("Mô tả không được bỏ trống")
            continue

        list_hashtag = input("Nhập hashtag, cách nhau bởi \",\":  ")

        print(f"Tên tài khoản sau khi loại bỏ khoảng trắng đầu và cuối: {user_name.strip()}")

        print(f"Tiêu đề sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ: {title_video.strip().title()}")

        processed_describe_video = describe_video.strip()
        print(f"Mô tả sau khi loại bỏ khoảng trắng đầu và cuối: {processed_describe_video}")

        print(f"Độ dài mô tả: {len(processed_describe_video)}")

        print(f"Số lượng từ trong mô tả video: {len(processed_describe_video.split(" "))}")

        print(f"Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {list_hashtag.strip()}")

        print(f"Số lượng hashtag: {len(list_hashtag.split(","))}")

        print(f"Mô tả video được chuyển toàn bộ sang chữ thường: {processed_describe_video.lower()}")

        print(f"Mô tả video được chuyển toàn bộ sang chữ hoa: {processed_describe_video.upper()}")

    elif choice == "2":
        if not user_name:
            print("Vui lòng nhập tên tài khoản trước (chức năng 1).")
        else:
            formatted_name = "@" + user_name.strip().lower()

            print(f"Tên tài khoản sau khi chuẩn hóa: {formatted_name}")

    elif choice == "3":
        hashtag = input("Nhập vào một hashtag")
        if not hashtag.strip():
            print("Hashtag không được để trống")

        if not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        if len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")

        is_valid_hashtag = True
        for char in hashtag[1:]:
            if not (char.isalnum() or char == "_"):
                print("Hashtag chứa ký tự không hợp lệ")
                is_valid_hashtag = False
                break

        if is_valid_hashtag:
            print("Hashtag hợp lệ")
            list_hashtag = list_hashtag + "," + hashtag

    elif choice == "4":
        if not describe_video.strip():
            print("Chưa có mô tả video. Vui lòng nhập dữ liệu ở chức năng 1.")
            continue

        keyword_search = input("Nhập từ khoá cần tìm: ")
        keyword_replace = input("Nhập từ khoá thay thế: ")

        if keyword_search in describe_video:
            count = describe_video.count(keyword_search)

            new_describe_video = describe_video.replace(keyword_search, keyword_replace)

            print(f"Mô tả sau khi thay thế: {new_describe_video}")
            print(f"Số lần xuất hiện: {count}")
        else:
            print("Không tìm thấy từ khoá trong mô tả video.")

    elif choice == "5":
        print("Thoát chương trình")
        break