import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def parse_product(product):
    try:
        product_id, name, price, rating = product.split("-")
        if not price.isdigit():
            raise ValueError
        return (
            product_id,
            name,
            int(price),
            float(rating)
        )
    except ValueError:
        product_id = product.split("-")[0]
        print(
            f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu"
        )
        return None

    except IndexError:
        product_id = product.split("-")[0]
        print(
            f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu"
        )
        return None

def display_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    template = (
        "Mã: {id:<10} | "
        "Tên: {name:<20} | "
        "Giá: {price} VND | "
        "Rating: {rating}*"
    )
    for product in product_list:
        data = parse_product(product)
        if data is None:
            continue
        product_id, name, price, rating = data
        product_info = {
            "id": product_id,
            "name": name,
            "price": f"{price:,}",
            "rating": rating
        }
        print(
            template.format_map(product_info)
        )

def sort_key(product):
    data = parse_product(product)
    if data is None:
        return (999999, 999999)
    _, _, price, rating = data
    return (-rating, price)

def smart_sort_products():
    product_list.sort(key=sort_key)
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for index, product in enumerate(product_list, 1):
        print(f"{index}. {product}")

def calculate_inventory_value():
    prices = []
    for product in product_list:
        data = parse_product(product)
        if data is None:
            continue
        prices.append(data[2])

    if len(prices) == 0:
        total = 0
    else:
        total = functools.reduce(
            lambda acc, x: acc + x,
            prices
        )
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(
        f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND."
    )
    return total

while True:
    print("\n============= E-COMMERCE ANALYTICS =============")
    print("1. Hiển thị tem nhãn sản phẩm")
    print("2. Sắp xếp sản phẩm thông minh")
    print("3. Tính tổng giá trị kho hàng")
    print("4. Đóng hệ thống")
    print("================================================")

    choice = input(
        "Chọn chức năng (1-4): "
    ).strip()

    if choice == "1":
        display_labels()

    elif choice == "2":
        smart_sort_products()

    elif choice == "3":
        calculate_inventory_value()

    elif choice == "4":
        print(
            "\nĐóng hệ thống E-Commerce Analytics..."
        )
        break

    else:
        print(
            "Lựa chọn không hợp lệ!"
        )