playlist = []

while True:
    print("\n========== QUẢN LÝ PLAYLIST ==========")
    print("1. Thêm bài hát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát")
    print("4. Sắp xếp và Trích xuất")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        continue

    choice = int(choice)

    if choice == 1:
        print("\n1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí bất kỳ")

        sub_choice = input("Chọn: ").strip()

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub_choice = int(sub_choice)

        song_name = input("Nhập tên bài hát: ")

        if sub_choice == 1:
            playlist.append(song_name)

            print("Thêm bài hát thành công!")
            print("Số lượng bài hát:", len(playlist))

        elif sub_choice == 2:
            index = input("Nhập vị trí muốn chèn: ").strip()

            if not index.isdigit():
                print("Vị trí không hợp lệ.")
                continue

            index = int(index)

            if index < 1 or index > len(playlist) + 1:
                print("Vị trí không hợp lệ.")
                continue

            playlist.insert(index - 1, song_name)

            print("Chèn bài hát thành công!")
            print("Số lượng bài hát:", len(playlist))

        else:
            print("Lựa chọn không hợp lệ.")

    elif choice == 2:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n===== DANH SÁCH PHÁT =====")

        for i in range(len(playlist)):
            print(str(i + 1) + ". " + playlist[i])

    elif choice == 3:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n1. Xóa theo tên")
        print("2. Xóa theo số thứ tự")

        sub_choice = input("Chọn: ").strip()

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub_choice = int(sub_choice)

        if sub_choice == 1:

            song_name = input("Nhập tên bài hát cần xóa: ")

            if song_name in playlist:
                playlist.remove(song_name)
                print("Đã xóa bài hát", song_name, "khỏi danh sách")
            else:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub_choice == 2:

            index = input("Nhập số thứ tự cần xóa: ").strip()

            if not index.isdigit():
                print("Vị trí không hợp lệ.")
                continue

            index = int(index)

            if index < 1 or index > len(playlist):
                print("Vị trí không hợp lệ.")
                continue

            deleted_song = playlist.pop(index - 1)

            print("Đã xóa bài hát", deleted_song, "khỏi danh sách")

        else:
            print("Lựa chọn không hợp lệ.")

    elif choice == 4:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n1. Sắp xếp A-Z")
        print("2. Hiển thị 3 bài hát đầu tiên")

        sub_choice = input("Chọn: ").strip()

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub_choice = int(sub_choice)

        if sub_choice == 1:

            playlist.sort()

            print("\nDanh sách sau khi sắp xếp:")

            for i in range(len(playlist)):
                print(str(i + 1) + ". " + playlist[i])

        elif sub_choice == 2:

            print("\n3 bài hát đầu tiên:")

            first_three = playlist[:3]

            for i in range(len(first_three)):
                print(str(i + 1) + ". " + first_three[i])

        else:
            print("Lựa chọn không hợp lệ.")

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")