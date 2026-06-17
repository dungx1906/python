from datetime import datetime
from datetime import timedelta


def calculate_eta(flight_list):

    print(
        "----- TÍNH TOÁN THỜI GIAN "
        "HẠ CÁNH (ETA) -----"
    )

    flight_id = input(
        "Nhập mã chuyến bay cần tính: "
    ).strip().upper()

    for flight in flight_list:

        if flight["flight_id"] == flight_id:

            departure_datetime = (
                datetime.strptime(
                    flight["depart_time"],
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            estimated_arrival_time = (
                departure_datetime
                + timedelta(
                    minutes=flight["duration_min"]
                )
            )

            print(
                f"-> Chuyến bay {flight_id} "
                f"cất cánh lúc: "
                f"{flight['depart_time']}"
            )

            print(
                "-> Thời gian hạ cánh "
                f"dự kiến (ETA): "
                f"{estimated_arrival_time}"
            )

            return

    print(
        "Không tìm thấy chuyến bay!"
    )