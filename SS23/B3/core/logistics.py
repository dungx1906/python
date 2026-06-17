import math

def display_flights(flight_list):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for index, flight in enumerate(flight_list, start=1):

        backup_water_boxes = math.ceil(
            flight["passengers"] / 10
        )

        print(
            f"{index}. Mã: {flight['flight_id']} | "
            f"Khởi hành: {flight['depart_time']} | "
            f"Số khách: {flight['passengers']} | "
            f"Dự phòng: {backup_water_boxes} thùng nước."
        )