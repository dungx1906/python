# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),  # Tuyển thủ 1: Dữ liệu bình thường
    ("ShowMaker", "15", "0", "10"),  # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
    ("Chovy", "12", "ba", "5")  # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
]


# Hàm xử lý dồn cục, đặt tên biến kém
def calculate_kda(list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for value in list:
        name = value[0]
        kills = value[1]
        deaths = value[2]
        assists = value[3]

        # Ép kiểu và tính toán trực tiếp
        try:
            kda = (int(kills) + int(assists)) / int(deaths)

        except ZeroDivisionError:
            print(f"{name}: KDA HOÀN HẢO (Perfect Game)!")

        except ValueError:
            print(f"{name}: Lỗi dữ liệu hệ thống không hợp lệ!")

        else:
            print(f"{name}: Có chỉ số KDA là: {kda}")

# Chạy hệ thống
(calculate_kda(data))