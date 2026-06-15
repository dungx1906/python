import logging

logging.basicConfig(
    filename='roster_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


def get_valid_salary_input(prompt_text):
    while True:
        try:
            salary_input = input(prompt_text).strip()
            salary = float(salary_input)
            if salary <= 0:
                print('\nLương phải là số dương. Vui lòng nhập lại.')
                continue
            return salary
        except ValueError:
            print('\nLương phải là số. Vui lòng nhập lại.')
            logging.warning("Failed to sign player - Invalid salary input")


def display_roster(roster_list):
    if not roster_list:
        print('Đội hình hiện đang trống.')
        return

    print('\n--- ĐỘI HÌNH RIKKEI ESPORTS ---')
    header = f'{"ID":<8} | {"Tên tuyển thủ":<20} | {"Vị trí":<15} | {"Lương":<12} | {"Trạng thái"}'
    print(header)
    print("-" * 80)

    for player in roster_list:
        try:
            status = player.get("status", "Unknown")

            if status == "Benched":
                display_name = f'{player["name"]} [DỰ BỊ]'
            else:
                display_name = player["name"]

            formatted_salary = f'{player["salary"]:,.1f}'

            print(
                f'{player["player_id"]:<8} | {display_name:<20} | {player["role"]:<15} | {formatted_salary:<12} | {status}')
        except KeyError as e:
            logging.error(f"Missing key while displaying player info: {e}")
            print(f'Lỗi: Tuyển thủ có mã {player.get("player_id", "Không rõ")} bị thiếu dữ liệu.')

    logging.info("Coach viewed the team roster.")


def sign_player(roster_list):
    print('\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---')
    player_id = input('Nhập mã tuyển thủ: ').strip().upper()

    if not player_id:
        print('Mã tuyển thủ không được để trống.')
        return

    for player in roster_list:
        if player["player_id"] == player_id:
            print(f'\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.')
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return

    name = input('Nhập tên tuyển thủ: ').strip().title()
    role = input('Nhập vị trí thi đấu: ').strip().title()

    salary = get_valid_salary_input('Nhập mức lương hàng tháng: ')

    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }
    roster_list.append(new_player)

    print(f'\nThành công: Đã chiêu mộ tuyển thủ {name}.')
    logging.info(f"Signed new player {name} with salary {salary:.1f}")


def update_player_status(roster_list):
    print('\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---')
    player_id = input('Nhập mã tuyển thủ cần cập nhật: ').strip().upper()

    found_player = None
    for player in roster_list:
        if player["player_id"] == player_id:
            found_player = player
            break

    if not found_player:
        print(f'\nKhông tìm thấy tuyển thủ mang mã {player_id}.')
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return

    print(f'\nTuyển thủ: {found_player["name"]}')
    print(f'Vị trí: {found_player["role"]}')
    print(f'Lương hiện tại: {found_player["salary"]:,.1f}')
    print(f'Trạng thái hiện tại: {found_player["status"]}')

    print('\nBạn muốn cập nhật:')
    print('1. Cập nhật lương')
    print('2. Cập nhật trạng thái thi đấu')
    choice = input('Chọn chức năng cập nhật (1-2): ').strip()

    if choice == "1":
        old_salary = found_player["salary"]
        new_salary = get_valid_salary_input('Nhập mức lương mới: ')
        found_player["salary"] = new_salary
        print(f'\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}.')
        logging.info(f"Updated player {player_id} salary from {old_salary:.1f} to {new_salary:.1f}")

    elif choice == "2":
        print('\nChọn trạng thái mới:')
        print('1. Active')
        print('2. Benched')
        status_choice = input('Nhập lựa chọn trạng thái (1-2): ').strip()

        if status_choice == "1":
            found_player["status"] = "Active"
        elif status_choice == "2":
            found_player["status"] = "Benched"
        else:
            print('Lựa chọn trạng thái không hợp lệ.')
            return

        print(f'\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.')
        logging.info(f"Updated player {player_id} status to {found_player['status']}.")
    else:
        print('Lựa chọn không hợp lệ.')


def generate_payroll_report(roster_list):
    print('\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---')

    if not roster_list:
        print('Đội hình hiện đang trống. Tổng quỹ lương: 0.0')
        return

    print(f'{"ID":<8} | {"Tên tuyển thủ":<15} | {"Trạng thái":<10} | {"Lương gốc":<12} | {"Lương thực nhận"}')
    print("-" * 80)

    total_payroll = 0.0
    has_error = False

    for player in roster_list:
        try:
            salary = player["salary"]
            status = player.get("status", "Unknown")

            if status == "Active":
                actual_salary = salary
            elif status == "Benched":
                actual_salary = salary * 0.5
            else:
                actual_salary = salary

            total_payroll += actual_salary
            print(
                f'{player["player_id"]:<8} | {player["name"]:<15} | {status:<10} | {salary:,.1f} | {actual_salary:,.1f}')

        except KeyError as e:
            logging.error(f"Missing key while generating payroll report: {e}")
            has_error = True
            break

    print("-" * 80)
    if has_error:
        print('Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.')
        print("-" * 80)
        total_payroll = 0.0

    print(f'Tổng quỹ lương hàng tháng: {total_payroll:,.1f}')

    if not has_error:
        logging.info(f"Generated monthly payroll report. Total: {total_payroll:.1f}")


while True:
    print('''
===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS ===== 
1. Xem đội hình thi đấu hiện tại
2. Chiêu mộ tuyển thủ mới
3. Cập nhật lương & Trạng thái thi đấu
4. Báo cáo quỹ lương hàng tháng
5. Thoát hệ thống
==================================================''')

    menu_choice = input('Chọn chức năng (1-5): ').strip()

    match menu_choice:
        case "1":
            display_roster(roster)
        case "2":
            sign_player(roster)
        case "3":
            update_player_status(roster)
        case "4":
            generate_payroll_report(roster)
        case "5":
            print('Chương trình đã được thoát.')
            logging.info("System shutdown and application closed.")
            break
        case _:
            print('Lựa chọn không hợp lệ!! Vui lòng nhập số từ 1 đến 5.')
            logging.warning("Invalid menu choice selected.")