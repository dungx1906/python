player_records = [
    ("Levi", 120, 2500),  # Dữ liệu chuẩn
    ("SofM", 150),  # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")  # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]


def calculate_bonus(matches, mmr_str):
    """
    Hàm chuyên biệt để ép kiểu điểm MMR và tính toán tiền thưởng RP.
    Ném ra ValueError nếu MMR không phải định dạng số hợp lệ.
    """
    mmr = int(mmr_str)
    return (matches * 10) + (mmr * 0.5)


def process_rp_rewards(records_list):
    """
    Hàm chính duyệt danh sách tuyển thủ và in kết quả thưởng RP.
    Sử dụng try...except để cô lập lỗi, giúp vòng lặp không bị gián đoạn.
    """
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in records_list:
        try:
            # Lấy tên tuyển thủ (luôn ở index 0)
            player_name = record[0]

            # Khối lệnh có thể gây ra IndexError nếu tuple thiếu phần tử
            matches = record[1]
            mmr_data = record[2]

            # Gọi hàm tính toán (có thể gây ra ValueError)
            bonus_rp = calculate_bonus(matches, mmr_data)
            print(f"Tuyển thủ {player_name} nhận được {bonus_rp:.1f} RP")

        except IndexError:
            # Xử lý khi tuple bị thiếu thông tin (như trường hợp SofM)
            # Vì thiếu dữ liệu index 0 có thể vẫn có hoặc không, ta lấy từ record[0] nếu có thể
            player_name = record[0] if len(record) > 0 else "Ẩn danh"
            print(f"Tuyển thủ {player_name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue  # Tiếp tục chạy tuyển thủ phía sau

        except ValueError:
            # Xử lý khi lỗi ép kiểu dữ liệu MMR (như trường hợp Optimus)
            print(f"Tuyển thủ {player_name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue  # Tiếp tục chạy tuyển thủ phía sau

    print("--- HOÀN TẤT ---")


# Vận hành hệ thống trao thưởng
process_rp_rewards(player_records)