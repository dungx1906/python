inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

titel = "QUẢN LÝ KHO HÀNG - GROCERY STORE ".center(50)

menu = '''
1. Xem danh sách hàng tồn kho
2. Nhập thêm hàng hoá mới
3. Cập nhật số lượng tông kho theo ID
4. Thoát chương trình
'''

def show_list_inventory():
    print("chức năng 1:")
    print("--- DANH SÁCH HÀNG TỒN KHO ---")
    header = (f"{"ID":<10} | "
              f"{"Tên hàng hoá":<15} | "
              f"{"Số lượng tồn":<10}")

    print("-" * len(header))

    for item in inventory:
        print(f"{item["id"]:<10} | "
              f"{item["name"]:<15} | "
              f"{item["quantity"]:<10}")

    print("-" * len(header))

def append_new_inventory():
    new_inventory = {}

    while True:
        new_inventory["id"] = input("Nhập vào ID hàng hoá: ").strip()
        if len(new_inventory["id"]) == 0:
            print("Khồng được để trống!")
            continue
        else:
            break

    while True:
        new_inventory["name"] = input("Nhập vào tên hàng hoá: ").strip()
        if len(new_inventory["name"]) == 0:
            print("Khồng được để trống!")
            continue
        else:
            break

    while True:
        try:
            new_inventory["quantity"] = input("Nhập số lượng tồn kho: ")

        except ValueError:
            print("Vui lòng nhập vào số!")

        else:
            if int(new_inventory["quantity"]) > 0:
                break
            else:
                print("Vui lòng nhập số lớn hơn '0'!")

    print("Thêm hàng hoá vào kho thành công!")

    return new_inventory

while True:
    print("="*len(titel))
    print(titel)
    print("=" * len(titel))
    print(menu)
    print("=" * len(titel))
    try:
        choice = int(input("Nhập vào lựa chọn của bạn: "))

    except ValueError:
        print("Vui lòng nhập vào số!")

    else:
        match choice:
            case 1:
                # if len(inventory) == 0:
                #     print("Kho hàng hiện đang trống!")
                print(show_list_inventory())

            case 2:
                print("chức năng 2:")
                inventory.append(append_new_inventory())

            case 3:
                pass
                # print("chức năng 3:")
                # new_id = input("Nhập mã hàng hoá cần sửa: ")
                # for new_id in inventory:
                #     print(f"Tìm thấy hàng hoá: {inventory['name']} (Số lượng hiện tại: {inventory['quantity']}")
                #
                #     try:
                #          = input("Nhập số lượng mới: ")
                #
                #     except ValueError:
                #         print("Vui lòng nhập vào số!")
                #
                #     else:
                #         if new_quantity > 0:
                #             break
                #         else:
                #             print("Vui lòng nhập số lớn hơn '0'!")
                #

            case 4:
                print("Thoát chương trình!")
                break

            case _:
                print("Vui lòng nhập số trong khoảng (1-4)")