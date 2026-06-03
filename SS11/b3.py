product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 10}
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for index, product in enumerate(product_list, start=1):
                print(
                    f"{index}. Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )

    elif choice == "2":

        product_id = input("Nhập mã sản phẩm: ").strip().upper()

        is_duplicate = False

        for product in product_list:
            if product["product_id"] == product_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sản phẩm bị trùng")
            continue

        product_name = input("Nhập tên sản phẩm: ").strip()

        try:
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng sản phẩm: "))

            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue

        except:
            print("Giá/Số lượng không hợp lệ")
            continue

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }

        product_list.append(new_product)

        print("Thêm sản phẩm thành công")

    elif choice == "3":

        update_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == update_id:

                found = True

                new_name = input("Nhập tên mới: ").strip()

                try:
                    new_price = int(input("Nhập giá mới: "))
                    new_quantity = int(input("Nhập số lượng mới: "))

                    if new_price <= 0 or new_quantity <= 0:
                        print("Giá/Số lượng không hợp lệ")
                        break

                except:
                    print("Giá/Số lượng không hợp lệ")
                    break

                product["product_name"] = new_name
                product["price"] = new_price
                product["quantity"] = new_quantity

                print("Cập nhật sản phẩm thành công")
                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == "4":

        delete_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == delete_id:
                product_list.remove(product)
                found = True
                print("Xóa sản phẩm thành công")
                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")