cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n===== AMAZON CART MANAGEMENT =====")
    print("1. Xem giỏ hàng và tổng tiền")
    print("2. Thêm sản phẩm / Tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    # Chức năng 1
    if choice == 1:
        total_quantity = 0
        total_money = 0

        print("\nID\tTên sản phẩm\t\tSL\tĐơn giá")

        for item in cart_items:
            print(item["id"], "\t",
                  item["name"], "\t",
                  item["number"], "\t",
                  item["price"])

            total_quantity += item["number"]
            total_money += item["number"] * item["price"]

        print("Tổng số lượng:", total_quantity)
        print("Tổng tiền:", total_money, "VNĐ")

    # Chức năng 2
    elif choice == 2:
        product_id = input("Nhập mã sản phẩm: ")
        product_name = input("Nhập tên sản phẩm: ")

        quantity = input("Nhập số lượng: ")
        price = input("Nhập đơn giá: ")

        if not quantity.isdigit() or not price.isdigit():
            print("Số lượng và đơn giá phải là số!")
            continue

        quantity = int(quantity)
        price = int(price)

        if quantity <= 0 or price < 0:
            print("Dữ liệu không hợp lệ!")
            continue

        found = False

        for item in cart_items:
            if item["id"] == product_id:
                item["number"] += quantity
                found = True
                print("Đã tăng số lượng sản phẩm.")
                break

        if found == False:
            cart_items.append({
                "id": product_id,
                "name": product_name,
                "number": quantity,
                "price": price
            })
            print("Thêm sản phẩm thành công!")

    # Chức năng 3
    elif choice == 3:
        product_id = input("Nhập mã sản phẩm: ")
        new_quantity = input("Nhập số lượng mới: ")

        if not new_quantity.isdigit():
            print("Số lượng phải là số!")
            continue

        new_quantity = int(new_quantity)

        if new_quantity <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue

        found = False

        for item in cart_items:
            if item["id"] == product_id:
                item["number"] = new_quantity
                found = True
                print("Cập nhật thành công!")
                break

        if found == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    # Chức năng 4
    elif choice == 4:
        product_id = input("Nhập mã sản phẩm cần xóa: ")

        found = False

        for item in cart_items:
            if item["id"] == product_id:
                cart_items.remove(item)
                found = True
                print("Xóa sản phẩm thành công!")
                break

        if found == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    # Chức năng 5
    elif choice == 5:
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn phải từ 1 đến 5.")