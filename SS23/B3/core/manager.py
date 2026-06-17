from datetime import datetime

def check_duplicate_id(flight_id, flight_list):

    normalized_flight_id = flight_id.strip().upper()

    for flight in flight_list:
        if flight["flight_id"] == normalized_flight_id:
            return True

    return False

def add_new_flight(flight_list):

    print("----- TIẾP NHẬN CHUYẾN BAY MỚI -----")

    flight_id = input(
        "Nhập mã chuyến bay: "
    ).strip().upper()

    if check_duplicate_id(
            flight_id,
            flight_list):

        print(
            "Mã chuyến bay đã tồn tại!"
        )
        return

    try:

        passenger_count = int(
            input(
                "Nhập số lượng hành khách: "
            )
        )

        departure_time = input(
            "Nhập thời gian cất cánh "
            "(YYYY-MM-DD HH:MM:SS): "
        )

        datetime.strptime(
            departure_time,
            "%Y-%m-%d %H:%M:%S"
        )

        flight_duration = int(
            input(
                "Nhập số phút bay: "
            )
        )

        new_flight = {
            "flight_id": flight_id,
            "passengers": passenger_count,
            "depart_time": departure_time,
            "duration_min": flight_duration
        }

        flight_list.append(
            new_flight
        )

        print(
            f">> Thêm chuyến bay "
            f"{flight_id} thành công!"
        )

    except ValueError:
        print(
            "Sai định dạng thời gian! "
            "Vui lòng nhập đúng chuẩn "
            "YYYY-MM-DD HH:MM:SS"
        )