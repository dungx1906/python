menu = """
========== HỆ THỐNG QUẢN LÝ PLAYLIST SPOTIFY ==========
1. Thêm bài hát mới & Phân tích dữ liệu
2. Quản lý danh sách phát
3. Tìm kiếm và thay thế tên bài hát
4. Sắp xếp danh sách phát
5. Thoát chương trình
=======================================================
"""

current_playlist = []
count = 0

def format_song_and_artist(string):
    while True:
        song_title = input(f"{string}").strip()
        if song_title:
            break
        print("Tên bài hát và tên nghệ sĩ không được để trống")

    return song_title

def display_menu(title, title_width, *options):
    header = f"{title}".center(title_width, "=")
    menu = ""
    for index, option in enumerate(options, 1):
        menu +=f"{index}. {option} \n"
    menu_footer = "=" * len(header)

    print(f"{header}\n{menu}{menu_footer}")

def input_detail_song( index_input:int):
    global current_playlist
    song_title = format_song_and_artist("Nhập tên bài hát:")
    artist_name = format_song_and_artist("Nhập tên nghệ sĩ:")
    genres_string = input("Nhập danh sách thể loại, cách nhau bởi dấu ',': ")

    song_title = song_title.title()
    artist_name = artist_name.upper()

    genre_list = genres_string.split(",")
    genre_list = [genre.strip() for genre in genre_list]

    result = " - ".join([song_title, artist_name])
    current_playlist.insert(index_input, result)

    print("Thông tin sau khi được chuyển hoá:")
    print(f"Tên bài hát: {song_title}")
    print(f"Nghệ sĩ: {artist_name}")
    print(f"Danh sách thể loại: {genre_list}")
    print(f"Số lượng thể loại: {len(genre_list)}")

    print(f"Đã thêm bài hát vào Playlist: {result}")
    return current_playlist


while True:
    display_menu("HỆ THỐNG QUẢN LÝ PLAYLIST SPOTIFY",
                 50,
                 "Thêm bài hát mới & Phân tích dữ liệu",
                 "Quản lý danh sách phát",
                 "Tìm kiếm và thay thế tên bài hát",
                 "Sắp xếp danh sách phát",
                 "Thoát chương trình")
    try:
        choice = int(input("Nhập vào lựa chọn: "))

    except ValueError:
        print("Vui lòng nhập số!")

    else:
        match choice:
            case 1:
                print("Chức năng 1:")

                input_detail_song(count)
                count += 1

            case 2:
                while True:
                    display_menu("QUẢN LÝ DANH SÁCH PHÁT",
                                 50,
                                 "Chèn bài hát vào vị trí bất kỳ",
                                 "Xóa bài hát theo tên chính xác",
                                 "Xoá bài hát cuối cùng",
                                 "Xem Playlist",
                                 "Quay lại menu chính")

                    try:
                        choice_case_2 = int(input("Nhập vào lựa chộn của bạn: "))
                    except ValueError:
                        print("Vui lòng nhập số!")
                    else:
                        match choice_case_2:
                            case 1:
                                print("--- CHÈN BÀI HÁT VÀO PLAYLIST ---")
                                try:
                                    index_insert = int(input("Nhập vào vị trí muốn tìm: "))
                                except ValueError:
                                    print("Vui lòng nhập số!")
                                else:
                                    if (index_insert <= -len(current_playlist) or (index_insert >= len(current_playlist))):
                                        print("Vị trí chèn không hợp lệ!")
                                        print("Bài hát sẽ được thêm vào cuối Playlist.")

                                    input_detail_song(index_insert)

                            case 2:
                                print("--- XOÁ BÀI HÁT THEO TÊN ---")
                                del_song_title = input("Nhập chính xác tên cần xoá: ")

                                if del_song_title in current_playlist:
                                    current_playlist.remove(del_song_title)
                                    print(f"Đã xoá bài hát ra khỏi Playlist: {del_song_title}")
                                else:
                                    print("Bài hát không tồn tại trong Playlist")

                            case 3:
                                print("--- XOÁ BÀI HÁT CUỐI CÙNG ---")
                                if len(current_playlist) > 0:
                                    del_song_output = current_playlist.pop()
                                    print(f"Đã xoá bài hát cuối cùng: {del_song_output}")
                                else:
                                    print("Playlist hiện đang trống, vui lòng thêm bài hát trước (chức năng 1).")
                            case 4:
                                header = "PLAYLIST HIỆN TẠI".center(30, "-")
                                list_song = ""
                                for index, item in enumerate(current_playlist, 1):
                                    list_song += f"{index}. {item}\n"
                                footer = "-" * len(header)

                                print(f"{header}\n{list_song + footer}")
                                print(f"Tồng số bài hát hiện tại: {len(current_playlist)}")

                            case 5:
                                print("Quay lại menu chính")
                                break


            case 3:
                if len(current_playlist) > 0:
                    print("--- TÌM KIẾM VÀ THAY THẾ TÊN BÀI HÁT ---")
                    search_keyword = input("Nhập vào từ khoá cần tìm: ").strip().lower()
                    replace_keyword = input("Nhập từ khoá cần thay thế: ").strip().lower()

                    total_replace = 0
                    print("Các từ khoá đã thay đổi:")
                    for index, item in enumerate(current_playlist, 1):

                        if search_keyword in item.lower():
                            old_item = item
                            new_item = item.replace(search_keyword, replace_keyword)
                            print(f"{index}. {old_item}     ->     {new_item}")
                            total_replace += 1

                    if total_replace:
                        print(f"Tổng số lần thay thế thành công: {total_replace}")
                    else:
                        print("Không tìm thấy bài hát nào chứa từ khoá này.")
                else:
                    print("Playlist hiện tại đang trống, vui lòng thêm bài trước (Chức năng 1)")

            case 4:
                while True:
                    print("--- SẾP DANH SÁCH PHÁT ---")
                    print("1. Sắp xếp A-Z")
                    print("2. Đảo ngược danh sách")
                    print("3. Thoát phần sắp xếp")
                    try:
                        choice_sort = int(input("Chọn kiểu sắp xếp: "))
                    except ValueError:
                        print("Vui lòng nhập số:")
                    else:
                        match choice_sort:
                            case 1:
                                list_song = ""
                                current_playlist.sort()
                                print("Đã sắp xếp Playlist theo thứ tự A-Z\n")
                                for index, item in enumerate(current_playlist, 1):
                                    list_song += f"{index}. {item}\n"

                                print("--- PLAYLIST SAU KHI ĐƯỢC SẮP XẾP ---")
                                print(list_song)

                            case 2:
                                current_playlist.reverse()
                                print("Đã đảo ngược thứ tự Playlist.")
                                list_song = ""
                                for index, item in enumerate(current_playlist, 1):
                                    list_song += f"{index}. {item}\n"

                                print("--- PLAYLIST SAU KHI ĐẢO NGƯỢC ---")
                                print(list_song)

                            case 3:
                                print("Thoát phần sắp xếp")
                                break

                            case _:
                                print("Vui lòng nhập trong khoảng (1-2)")


            case 5:
                print("Thoát chương trình!")
                break

            case _:
                print("Nhập sai mời nhập lại!")
