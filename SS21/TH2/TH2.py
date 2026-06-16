import logging


logging.basicConfig(
    filename='output.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'

)


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


class ItemNotFoundError(Exception):
    """Lỗi xảy ra khi mã đồ uống không tồn tại trong thực đơn."""
    pass


class InvalidQuantityError(Exception):
    """Lỗi xảy ra khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""
    pass



def view_menu():
    """Hiển thị danh sách thực đơn đồ uống hiện có."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():

        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def add_to_order(drink_code: str, quantity_str: str):
    """
    Kiểm tra dữ liệu đầu vào và thêm món ăn vào giỏ hàng.
    Bắn ra các ngoại lệ tương ứng nếu dữ liệu không hợp lệ.
    """
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {drink_code}")
        raise ItemNotFoundError("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")

    try:
        quantity = int(quantity_str)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        raise ValueError("Vui lòng nhập số lượng là một số nguyên!")


    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError("Số lượng phải lớn hơn 0!")

    logging.info(f"Added {quantity} of {drink_code} to order")

    for item in current_order:
        if item["code"] == drink_code:
            item["quantity"] += quantity
            break
    else:

        current_order.append({
            "code": drink_code,
            "name": DRINK_MENU[drink_code]["name"],
            "price": DRINK_MENU[drink_code]["price"],
            "quantity": quantity
        })

    print(f"Đã thêm {quantity} x {DRINK_MENU[drink_code]['name']} vào giỏ hàng.")


def calculate_total(order_list: list) -> int:
    """Tính tổng tiền của danh sách giỏ hàng truyền vào."""
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def view_order():
    """Hiển thị chi tiết giỏ hàng hiện tại và tổng chi phí."""
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return False

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<6} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)

    for item in current_order:
        subtotal = item["price"] * item["quantity"]
        print(
            f"{item['code']:<6} | {item['name']:<20} | {item['price']:,:<8} | {item['quantity']:<8} | {subtotal:,} VNĐ")

    print("-" * 64)
    total_amount = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")
    return True


def checkout():
    """Xử lý thủ tục thanh toán và làm trống giỏ hàng."""
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- THANH TOÁN ---")
    total_amount = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")

    confirm = input(f"Xác nhận thanh toán {total_amount:,} VNĐ? (y/n): ").strip().lower()

    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        current_order.clear()
        print("Giỏ hàng đã được làm trống.")
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def main():
    """Vòng lặp chính điều khiển giao diện Menu CLI."""
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            view_menu()

        elif choice == "2":
            print("\n--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ")
            quantity_str = input("Nhập số lượng: ")

            try:
                add_to_order(drink_code, quantity_str)
            except (ItemNotFoundError, InvalidQuantityError, ValueError) as e:
                print(e)

        elif choice == "3":
            view_order()

        elif choice == "4":
            checkout()

        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break

        else:
            print("Chức năng không hợp lệ, vui lòng chọn từ 1 đến 5!")


if __name__ == "__main__":
    main()