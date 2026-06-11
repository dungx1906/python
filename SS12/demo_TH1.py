
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
    demarcate = "=" * 50
    title = "SHOPEE CART MANAGEMENT SYSTEM".center(50)
    menu = """
[1] Xem chi tiết giỏ hàng & Tính tổng tiền
[2] Thêm sản phẩm mới / Cộng dồn số lượng
[3] Cập nhật số lượng của một sản phẩm
[4] Xoá sản phẩm khỏi giỏ hàng
[5] Thoát chương trình
"""

    print(f"{demarcate}\n{title}\n{demarcate}{menu}{demarcate}")

    try:
        choice = int(input("Nhập vào lựa chọn của bạn: "))
    except ValueError:
        print("Mời bạn nhập số!")

    else:
        match choice:
            case 1:
                print("chức năng 1")
                title_case_1 = " CHI TIẾT GIỎ HÀNG ".center(30,"-")
                header = f"{'STT':<5} | {'Mã SP':<7} | {'Tên Sản Phẩm':<25} | {'SL':<5} | {'Đơn Giá':<15} | {'Thành Tiền':<15}"
                print(title_case_1)
                print(header)
                print("-"*len(header))

                total_product = 0
                total_money = 0
                for index, item in enumerate(cart_items, 1):
                    into_money = item['number'] * item['price']
                    print(f"{index:<5} | "
                          f"{item['id']:<7} | "
                          f"{item['name']:<25} | "
                          f"{item['number']:<5} | "
                          f"{item['price']:<15,}đ | "
                          f"{into_money:,}đ")
                    total_product += item['number']
                    total_money += into_money

                print("-" * len(header))

                print(f"=> Tổng số lượng sản phẩm trong giỏ: {total_product}")
                print(f"=> TỔNG TIỀN THANH TOÁN: {total_money:,}")

            case 2:
                print("chức năng 2")
                product_id = input("Nhập mã sản phẩm: ")
                product_number = int(input("Nhập số lượng: "))

                check = False
                for item in cart_items:
                    if item['id'] == product_id:
                        item['number'] += product_number
                        check = True
                        print("Mã sản phẩm đã tồn tại, đã cộng dồn vào số lượng!")
                        break

                if not check:
                    product_price = int(input("Nhập đơn giá: "))
                    product_name = input("Nhập tên sản phẩm: ")
                    new_product = {
                        "id": product_id,
                        "name": product_name,
                        "number": product_number,
                        "price": product_price
                    }
                    cart_items = cart_items.append(new_product)
                    print("Đã thêm sản phẩm mới vào giỏ hàng")

            case 3:
                print("chức năng 3")
                product_id = input("Nhập mã sản phẩm: ")
                product_number = int(input("Nhập số lượng: "))

                check = False
                for item in cart_items:
                    if item['id'] == product_id:
                        item['number'] = product_number
                        check = True
                        print("Mã sản phẩm đã tồn tại, đã cập nhập số lượng")
                        break

                if not check:
                    print("mã sản phẩm không tônf tại")

            case 4:
                print("chức năng 1")

            case 5:
                print("Thoát chương trình")
                break

            case _:
                print("Mời bạn nhập lựa chọn trong vòng (1-5)")