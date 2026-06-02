while True:
    print('+==============================================+')
    print('|  HỆ THÔNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPEE  |')
    print('+==============================================+')
    print('1. Nhập dữ liệu sản phẩm và báo cáo thống kê   |')
    print('2. Chuẩn hóa tên shop                          |')
    print('3. Kiểm tra mã giảm giá hợp lệ                 |')
    print('4. Tìm kiếm và thay thế từ khóa trong mô tả    |')
    print('5. Thoát chương trình                          |')
    print('+==============================================+')

    choice = input('Mời bạn chọn chức năng (1-5):')

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    if int(choice) not in range(1, 6):
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    if choice == "1":
        shop_name = input("Nhập tên shop: ")
        if not shop_name.strip():
            print("Tên shop không được bỏ trống: ")
            continue

        product_name = input("Nhâp tên sản phẩm: ")

        describe_product = input("Nhập mô tả sản phẩm: ")
        if not describe_product.strip():
            print("Mô tả sản phẩm không được bỏ trống")
            continue

        category_product = input("Nhập doanh mục sản phẩm: ")

        list_keywords = input("Nhập danh sách từ khoá tìm kiếm, cách nhau bởi \",\":  ")

        list_discount_code = ""

        print(f"Tên tài khoản sau khi loại bỏ khoảng trắng đầu và cuối: {shop_name.strip()}")

        print(f"Tên sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ: {product_name.strip().title()}")

        processed_describe_product = describe_product.strip()
        print(f"Mô tả sau khi loại bỏ khoảng trắng đầu và cuối: {processed_describe_product}")

        print(f"Độ dài mô tả: {len(processed_describe_product)}")

        print(f"Số lượng từ trong mô tả video: {len(processed_describe_product.split(" "))}")

        print(f"Danh mục sản phẩm sau khi chuẩn hóa khoảng trắng, chuyển hoá thành chữ thường: {category_product.strip().lower()}")

        print(f"Danh sách từ khoá sau khi chuẩn hóa khoảng trắng{list_keywords.strip()}")

        print(f"Số lượng từ khoá tìm kiếm: {len(list_keywords.split(","))}")

        print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ thường: {processed_describe_product.lower()}")

        print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa: {processed_describe_product.upper()}")

    elif choice == "2":
        if not shop_name:
            print("Vui lòng nhập tên shop trước (chức năng 1).")
        else:
            formatted_shop = "shop-" + shop_name.lower().replace(" ", "-")

            print(f"Tên shop sau khi chuẩn hóa: {formatted_shop}")

    elif choice == "3":
        discount_code = input("Nhập vào một mã giảm giá")
        if not discount_code:
            print("mã giảm giá không được để trống")

        if not discount_code.strip():
            print("mã giảm giá không được để chứa khoảng trắng")

        if len(discount_code) < 12 and len(discount_code) > 6:
            print("mã giảm giá phải có độ dài từ 6 đến 12 ký tự")

        if not discount_code.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")

        is_valid_discount_code = True
        if not discount_code.isalnum() :
            print("mã giảm giá chứa ký tự không hợp lệ")
            is_valid_discount_code = False

        if not discount_code.startswith("SALE"):
            print("mã giảm giá phải bắt đầu bằng chuỗi SALE")

        if is_valid_discount_code:
            print("Mã giảm giá hợp lệ")
            list_discount_code += "," + discount_code

    elif choice == "4":
        if not describe_product.strip():
            print("Chưa có mô tả sản phẩm. Vui lòng nhập dữ liệu ở chức năng 1.")
            continue

        keyword_search = input("Nhập từ khoá cần tìm: ")
        keyword_replace = input("Nhập từ khoá thay thế: ")

        if keyword_search in describe_product:
            count = describe_product.count(keyword_search)

            new_describe_product = describe_product.replace(keyword_search, keyword_replace)

            print(f"Mô tả sau khi thay thế: {new_describe_product}")
            print(f"Số lần xuất hiện: {count}")
        else:
            print("Không tìm thấy từ khoá trong mô tả sản phẩm.")

    elif choice == "5":
        print("Thoát chương trình")
        break