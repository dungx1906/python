import logging
import traceback

logging.basicConfig(
    filename='tournament_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


def display_matches(match_list):
    if len(match_list) == 0:
        print('Hiện chưa có trận đấu nào trong hệ thống.')
        return

    print('\n--- LỊCH THI ĐẤU & KẾT QUẢ ---')
    header = f'{"Mã trận":<7} | {"Đội A":<15} | {"Đội B":<15} | {"Tỷ số":<7} | {"Trạng thái":<10}'
    print(header)
    print("-" * 70)

    for match in match_list:
        try:
            # Bẫy 3: Phòng hờ trường hợp API thiếu key score_a hoặc score_b
            score_text = f'{match["score_a"]}-{match["score_b"]}'
            print(
                f'{match["match_id"]:<7} | {match["team_a"]:<15} | {match["team_b"]:<15} | {score_text:<7} | {match["status"]:<10}')
        except KeyError as e:
            logging.error(f"Missing key in match data: {e}")
            print(f"Lỗi dữ liệu trận đấu mã {match.get('match_id', 'Không rõ')}.")

    logging.info("User viewed the match list.")


def get_valid_score(team_label):
    while True:
        try:
            score_input = input(f'Nhập điểm {team_label}: ')
            score = int(score_input)
            if score < 0:
                print('Điểm số phải lớn hơn hoặc bằng 0.')
                logging.error(f"Negative score input detected: {score}")
                continue
            return score
        except ValueError as e:
            print('Điểm số phải là số nguyên. Vui lòng nhập lại.')
            logging.error(f"Invalid score input. Error: invalid literal for int() with base 10: '{score_input}'")

def update_score(match_list):
    print('\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---')
    id_update = input('Nhập mã trận đấu cần cập nhật: ').strip().upper()

    found_match = None
    for match in match_list:
        if match["match_id"] == id_update:
            found_match = match
            break

    if not found_match:
        print(f'Không tìm thấy trận đấu mang mã {id_update}.')
        logging.warning(f"User tried to update non-existing match {id_update}")
        return

    print(f'\nTrận đấu: {found_match["team_a"]} vs {found_match["team_b"]} ({found_match["status"]})')

    new_score_a = get_valid_score(f'Đội A ({found_match["team_a"]})')
    new_score_b = get_valid_score(f'Đội B ({found_match["team_b"]})')

    # Bẫy 1 — Xử lý logic ẩn khi tỷ số là 0-0
    is_completed = True
    if new_score_a == 0 and new_score_b == 0:
        confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm != 'y':
            is_completed = False

    # Tiến hành cập nhật
    found_match["score_a"] = new_score_a
    found_match["score_b"] = new_score_b

    if is_completed:
        found_match["status"] = "Completed"
    else:
        found_match["status"] = "Pending"

    print(f'\nThành công: Đã cập nhật tỷ số trận đấu {id_update}.')
    logging.info(f"Match {id_update} score updated successfully")


def determine_winner(match):
    try:
        if match["status"] == "Pending":
            return "Not Started"
        if match["score_a"] > match["score_b"]:
            return match["team_a"]
        elif match["score_b"] > match["score_a"]:
            return match["team_b"]
        else:
            return "Draw"
    except KeyError:
        return "Data Error"


def generate_report(match_list):
    print('\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---')
    completed_count = 0

    for match in match_list:
        if match.get("status") == "Completed":
            winner = determine_winner(match)

            result_text = "Hòa" if winner == "Draw" else winner
            print(
                f'{match["match_id"]}: {match["team_a"]} {match["score_a"]}-{match["score_b"]} {match["team_b"]} | Kết quả: {result_text}')
            completed_count += 1

    if completed_count == 0:
        print('Chưa có trận đấu nào hoàn thành.')

    print(f'\nTổng số trận đã hoàn thành: {completed_count}')
    logging.info("User generated tournament report.")

while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====
1. Hiển thị lịch thi đấu & Kết quả
2. Thêm trận đấu mới
3. Cập nhật tỷ số trận đấu
4. Báo cáo thống kê
5. Thoát chương trình
================================================== 
Chọn chức năng (1-5):  ''').strip()

    match choice:
        case "1":
            display_matches(matches)

        case "2":
            print('\n--- THÊM TRẬN ĐẤU MỚI ---')

            id_add = input('Nhập mã trận đấu: ').strip().upper()
            if id_add == "":
                print('Mã trận đấu không được để trống.')
                logging.warning("User tried to add a match with empty match ID.")
                continue

            duplicate = False
            for value in matches:
                if value["match_id"] == id_add:
                    print(f'Lỗi: Mã trận đấu {id_add} đã tồn tại.')
                    logging.warning(f"Match ID {id_add} already exists.")
                    duplicate = True
                    break
            if duplicate:
                continue

            name_a = input('Nhập tên Đội A: ').strip()
            if name_a == "":
                print('Tên đội không được để trống.')
                logging.warning("User tried to add a match with empty team name.")
                continue

            name_b = input('Nhập tên Đội B: ').strip()
            if name_b == "":
                print('Tên đội không được để trống.')
                logging.warning("User tried to add a match with empty team name.")
                continue

            matches.append({
                "match_id": id_add,
                "team_a": name_a,
                "team_b": name_b,
                "score_a": 0,
                "score_b": 0,
                "status": "Pending"
            })
            print(f'\nThành công: Đã thêm trận đấu {id_add}.')
            logging.info(f"Match {id_add} added successfully")

        case "3":
            update_score(matches)

        case "4":
            generate_report(matches)

        case "5":
            print('Chương trình đã được thoát.')
            logging.info("System shutdown and application closed.")
            break

        case _:
            print('Lựa chọn không hợp lệ!! Vui lòng chọn từ 1 đến 5.')
            logging.warning("Invalid menu choice selected.")