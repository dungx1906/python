# {'id': int, 'type': str, 'owner': str}
smart_parking = []
is_car_true = False
automatically_increase = 1

while True:
    print("=========================================")
    print("     QUẢN LÝ BÃI XE - SMART PARKING      ")
    print("=========================================")
    print("1. Thêm xe mới vào bãi")
    print("2. Hiển thị danh sách xe trong bãi")
    print("3. Xoá xe khỏi bãi(khi xe ra)")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        while not is_car_true:
            car_type = input("Nhập vào loại xe: ")

            if not car_type.strip():
                print("Nhập sai mời nhập lại!")
                continue

            car_owner = input("nhập vào chủ xe:")

            if not car_owner.strip():
                print("Nhập sai mời nhập lại!")
                continue

            is_car_true = True
        is_car_true = False
        smart_parking.append(
            {
                'id': automatically_increase ,
                'type': car_type,
                'owner': car_owner
            }
        )
        automatically_increase += 1

    if choice == "2":
        if len(smart_parking) == 0:
            print("Bãi hiện tại đang trống!")

        else:
            header = f"{'id':<5} | {'loại xe':<10} | {'Chủ xe':<10}"
            print(header)
            print("-"*len(header))
            for i in smart_parking:
                print(f"{i['id']:<5} | {i['type']:<10} | {i['owner']:<10}")

    if choice == "4":
        print("Thoát chương trình")
        break


