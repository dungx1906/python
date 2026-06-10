import itertools

teams_list = []
match_schedule = []

def load_teams():
    global teams_list
    print("\n--- NHẬP DANH SÁCH ---")
    teams = input(
        "Nhập các đội (cách nhau bởi dấu phẩy): "
    )
    teams = [
        team.strip().upper()
        for team in teams.split(",")
        if team.strip()
    ]
    unique_teams = []
    for team in teams:
        if team not in unique_teams:
            unique_teams.append(team)
    teams_list = unique_teams
    print(
        f"Đã ghi nhận {len(teams_list)} đội: {teams_list}"
    )

def create_match_schedule():
    global match_schedule
    if len(teams_list) < 2:
        print(
            "Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu."
        )
        return
    matches = itertools.combinations(
        teams_list,
        2
    )

    match_schedule = [
        f"{team_a} vs {team_b}"
        for team_a, team_b in matches
    ]
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    for index, match in enumerate(
        match_schedule,
        1
    ):
        print(f"{index}. {match}")
    print(
        f"Tổng số trận đấu: {len(match_schedule)} trận."
    )

def generate_match_ids():
    if len(match_schedule) == 0:
        print(
            "Vui lòng tạo lịch thi đấu trước khi sinh mã ID."
        )
        return
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    for index, match in enumerate(
        match_schedule,
        1
    ):
        team_a, team_b = match.split(" vs ")
        team_a_code = f"{team_a[:3]:X<3}"
        team_b_code = f"{team_b[:3]:X<3}"
        match_id = (
            f"M{index:02d}-"
            f"{team_a_code}-"
            f"{team_b_code}"
        )
        print(
            f"Trận {index} ({match}) -> ID: {match_id}"
        )

while True:

    print("\n============= ESPORTS MATCHMAKER =============")
    print("1. Nhập danh sách Đội tuyển")
    print("2. Tạo lịch thi đấu (Combinations)")
    print("3. Tạo mã trận đấu tự động")
    print("4. Đóng hệ thống")
    print("==============================================")

    try:

        choice = int(
            input("Chọn chức năng (1-4): ")
        )
        match choice:
            case 1:
                load_teams()

            case 2:
                create_match_schedule()

            case 3:
                generate_match_ids()

            case 4:
                print(
                    "\nĐóng hệ thống Esports Matchmaker..."
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ!"
                )

    except ValueError:
        print(
            "Vui lòng nhập một số từ 1 đến 4!"
        )