cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n========== SHOPEE CART MANAGEMENT ==========")
    print("1. Xem chi tiết giỏ hàng")
    print("2. Thêm sản phẩm mới hoặc tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        if len(cart_items) == 0:
            print("Giỏ hàng đang trống!")
            continue

        print("\n{:<10} {:<25} {:<10} {:<15} {:<15}".format(
            "Ma SP", "Ten SP", "So Luong", "Don Gia", "Thanh Tien"
        ))

        total_quantity = 0
        total_money = 0

        for item in cart_items:
            amount = item[2] * item[3]

            total_quantity += item[2]
            total_money += amount

            print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
                item[0],
                item[1],
                item[2],
                item[3],
                amount
            ))

        print("-" * 80)
        print("Tổng số lượng sản phẩm:", total_quantity)
        print("Tổng tiền:", total_money)

    elif choice == 2:
        product_id = input("Nhập mã sản phẩm: ").strip()
        product_name = input("Nhập tên sản phẩm: ").strip()

        quantity = input("Nhập số lượng: ").strip()
        price = input("Nhập đơn giá: ").strip()

        if not quantity.isdigit() or not price.isdigit():
            print("Số lượng và đơn giá phải là số!")
            continue

        quantity = int(quantity)
        price = int(price)

        if quantity <= 0 or price < 0:
            print("Số lượng hoặc đơn giá không hợp lệ!")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] += quantity
                found = True
                print("Sản phẩm đã tồn tại. Đã cộng dồn số lượng.")
                break

        if not found:
            cart_items.append(
                [product_id, product_name, quantity, price]
            )
            print("Thêm sản phẩm mới thành công!")

    elif choice == 3:
        product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip()

        new_quantity = input("Nhập số lượng mới: ").strip()

        if not new_quantity.isdigit():
            print("Số lượng phải là số!")
            continue

        new_quantity = int(new_quantity)

        if new_quantity <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] = new_quantity
                found = True
                print("Cập nhật số lượng thành công!")
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == 4:
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip()

        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                found = True
                print("Xóa sản phẩm thành công!")
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == 5:
        print("Thoát chương trình!")
        break

    else:
        print("Vui lòng nhập từ 1 đến 5!")