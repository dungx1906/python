parking_lot = []
next_id = 1

while True:

    print("\n========== SMART PARKING SYSTEM ==========")
    print("1. Check-in xe")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out xe")
    print("5. Thoát")

    choice = input("Chọn chức năng: ")

    if not choice.isdigit():
        print("ERR-01: Lựa chọn không hợp lệ!")
        continue


    if choice == "1":

        plate = input("Nhập biển số xe: ").strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue

        duplicate = False

        for vehicle in parking_lot:
            if vehicle["plate"] == plate:
                duplicate = True
                break

        if duplicate:
            print("ERR-03: Biển số đã tồn tại trong bãi!")
            continue

        while True:

            vehicle_type = input(
                "Loại xe (1-Xe máy, 2-Ô tô): "
            )

            if vehicle_type.isdigit():

                vehicle_type = int(vehicle_type)

                if vehicle_type == 1:
                    vehicle_type = "Xe máy"
                    break

                elif vehicle_type == 2:
                    vehicle_type = "Ô tô"
                    break

            print("ERR-01: Loại xe không hợp lệ!")

        while True:

            entry_time = input(
                "Nhập giờ vào (0-23): "
            )

            if entry_time.isdigit():
                entry_time = int(entry_time)

                if 0 <= entry_time <= 23:
                    break

            print("ERR-01: Giờ vào không hợp lệ!")

        parking_lot.append(
            {
                "id": next_id,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time
            }
        )

        print("Check-in thành công!")

        next_id += 1

    elif choice == "2":

        if len(parking_lot) == 0:
            print("ERR-02: Bãi xe hiện đang trống!")
        else:

            print("\nDANH SÁCH XE TRONG BÃI")

            print(
                f"{'ID':<6}"
                f"{'Biển số':<15}"
                f"{'Loại xe':<15}"
                f"{'Giờ vào':<10}"
            )

            print("-" * 50)

            for vehicle in parking_lot:

                print(
                    f"{vehicle['id']:<6}"
                    f"{vehicle['plate']:<15}"
                    f"{vehicle['type']:<15}"
                    f"{vehicle['entry_time']:<10}"
                )

    elif choice == "3":

        plate = input(
            "Nhập biển số cần tìm: "
        ).strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue

        found = False

        for vehicle in parking_lot:

            if vehicle["plate"] == plate:

                found = True

                print("\nThông tin xe:")

                print(vehicle)

                break

        if not found:
            print("ERR-04: Không tìm thấy xe!")

    elif choice == "4":

        plate = input(
            "Nhập biển số cần check-out: "
        ).strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue

        found = False

        for vehicle in parking_lot:

            if vehicle["plate"] == plate:

                found = True

                while True:

                    exit_time = input(
                        "Nhập giờ ra (0-23): "
                    )

                    if exit_time.isdigit():

                        exit_time = int(exit_time)

                        if 0 <= exit_time <= 23:

                            if exit_time >= vehicle["entry_time"]:
                                break

                            else:
                                print(
                                    "ERR-05: Giờ ra phải lớn hơn hoặc bằng giờ vào!"
                                )
                                continue

                    print("ERR-01: Giờ ra không hợp lệ!")

                parking_hours = (
                    exit_time - vehicle["entry_time"]
                )

                if vehicle["type"] == "Xe máy":
                    fee = parking_hours * 5000
                else:
                    fee = parking_hours * 20000

                print("\n===== HÓA ĐƠN =====")
                print("Biển số:", vehicle["plate"])
                print("Loại xe:", vehicle["type"])
                print("Số giờ gửi:", parking_hours)
                print("Phí gửi xe:", fee, "VNĐ")

                parking_lot.remove(vehicle)

                print("Check-out thành công!")

                break

        if not found:
            print("ERR-04: Không tìm thấy xe!")

    elif choice == "5":

        print("Đã thoát chương trình!")
        break

    else:
        print("ERR-01: Lựa chọn không hợp lệ!")
    