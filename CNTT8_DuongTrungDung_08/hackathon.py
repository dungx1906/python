car_details_list = {
    "id":"XE001",
    "license_plate":"29C-12345(Tài A)",
    "consumption_rate":"12",
    "total_km":"500",
    "fuel_consumption":"65",
    "consumer_disparity_index":"5.0",
    "operating_performance_status":"Tiêu hao cao"
}

menu = """
1. Hiển thị danh sách đội xe
2. Bổ xung xe mới vào đội
3. Cập nhật nhật ký hành trình
4. Xoá xe khỏi đội quản lý
5. Tìm kiếm phương tiện
6. Thống kê hiệu xuất hạm đội
7. Phân loại hiệu xuất tự động
8. Thoát chương trình
"""

titel = "QUẢN LÝ ĐỘI XE".center(30,"-")

def output_list_car():
    titel_car_fleet = "DANH SÁCH ĐỘI XE".center(30, "-")
    print("-" * len(titel_car_fleet))
    for index, item in enumerate(car_details_list, 1):
        print(f"{index} | "
              f"{item["id"]} | "
              f"{item['license_plate']:<15} | "
              f"{item['consumption_rate']:<15} | "
              f"{item['total_km']:<8} | "
              f"{item['fuel_consumption']:<10} | "
              f"{item['consumer_disparity_index']:<17} | "
              f"{item['operating_performance_status']:<20}")

    print("-" * len(titel_car_fleet))

def input_car():
    global car_details_list
    new_car = {}
    print("chức năng 2")
    new_car['id_car'] = input("Nhập mã xe:")
    new_car['license_plate_car'] = input("Nhập Biển số xe: ")
    new_car['consumption_rate'] = int(input("Nhập định mức: "))
    new_car['total_km_car'] = input("Nhập số km chạy: ")
    new_car['fuel_consumption_car'] = int(input("Nhập số nhiên liệu tiêu hao thực tế:"))
    theoretical_consumption = new_car['total_km_car'] * new_car['consumption_rate'] / 100
    new_car['consumer_disparity_index_car'] = new_car['fuel_consumption_car'] - theoretical_consumption

    if new_car['consumer_disparity_index_car'] > 8:
        new_car['operating_performance_status'] = "Quá tải / Thất thoát"

    elif new_car['consumer_disparity_index_car'] >= 2:
        new_car['operating_performance_status'] = "Tiêu hao cao"

    elif new_car['consumer_disparity_index_car'] >= 0:
        new_car['operating_performance_status'] = "Tiêu chuẩn"

    else:
        new_car['operating_performance_status'] = "Tiết kiệm"



    return

while True:
    print(f"{"_"*len(titel)}\n{titel}\n{"_"*len(titel)}{menu}{"_"*len(titel)}")

    try:
        choice = int(input("Nhập vào lựa chọn của bạn: "))

    except ValueError:
        print("Mời bạn nhập số!")

    else:
        match choice:
            case 1:
                print("chức năng 1")
                # output_list_car()
                print(car_details_list)

            case 2:
                print(input_car())

            case 3:
                print("chức năng 3")

            case 4:
                print("chức năng 1")

            case 5:
                print("chức năng 1")

            case 6:
                print("chức năng 1")

            case 7:
                print("chức năng 1")

            case 8:
                print("Thoát chương trình")
                break

            case _:
                print("Vui lòng chọn trong khoảng (1-8)")
