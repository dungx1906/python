class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price +
            (self.__base_price * MenuItem.service_charge)
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        return (
            len(item_code) == 4
            and item_code[:2].isalpha()
            and item_code[:2].isupper()
            and item_code[2:].isdigit()
        )


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")
    print("===================================================")

    try:
        choice = int(input("Chọn chức năng (1-6): "))
    except ValueError:
        print("Vui lòng nhập số từ 1 đến 6!")
        continue

    match choice:
        case 1:
            print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

            for index, item in enumerate(menu_db, 1):
                status = (
                    "Đang bán"
                    if item.is_available
                    else "Hết hàng"
                )

                print(
                    f"{index}. Mã: {item.item_id} | "
                    f"Tên: {item.item_name} | "
                    f"Trạng thái: {status} | "
                    f"Giá niêm yết: "
                    f"{item.calculate_selling_price():,} VNĐ"
                )

        case 2:
            print("\n--- THÊM MÓN MỚI VÀO MENU ---")

            item_id = input("Nhập mã món: ").strip().upper()

            if not MenuItem.is_valid_item_id(item_id):
                print("\nMã món không hợp lệ!")
                print(
                    "Mã món phải gồm 2 chữ cái in hoa "
                    "và 2 chữ số. Ví dụ: CF01."
                )
                continue

            if find_item(item_id):
                print("Mã món đã tồn tại!")
                continue

            item_name = input("Nhập tên món: ").title()

            try:
                base_price = int(input("Nhập giá gốc: "))
            except ValueError:
                print("Giá tiền không hợp lệ!")
                continue

            menu_db.append(
                MenuItem(
                    item_id,
                    item_name,
                    base_price
                )
            )

            print("\nThêm món mới thành công!")

        case 3:
            print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")

            item_id = input(
                "Nhập mã món cần cập nhật: "
            ).strip().upper()

            item = find_item(item_id)

            if not item:
                print("Không tìm thấy món!")
                continue

            item.toggle_availability()

            status = (
                "ĐANG BÁN"
                if item.is_available
                else "HẾT HÀNG"
            )

            print(
                f">> Đã cập nhật "
                f"{item.item_name} thành {status}!"
            )

        case 4:
            print(
                "\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---"
            )

            item_id = input(
                "Nhập mã món cần đổi giá: "
            ).strip().upper()

            item = find_item(item_id)

            if not item:
                print("Không tìm thấy món!")
                continue

            try:
                new_price = int(
                    input("Nhập giá tiền mới: ")
                )
            except ValueError:
                print("Giá tiền không hợp lệ!")
                continue

            item.base_price = new_price

        case 5:
            print(
                "\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ "
                "TOÀN HỆ THỐNG ---"
            )

            print(
                f"Phụ phí hiện tại: "
                f"{MenuItem.service_charge * 100:.0f}%"
            )

            try:
                new_rate = float(
                    input(
                        "Nhập phụ phí mới "
                        "(Ví dụ 0.1 = 10%): "
                    )
                )
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

            MenuItem.update_service_charge(new_rate)

            print(
                "Cập nhật phụ phí dịch vụ thành công!"
            )

        case 6:
            print(
                "Cảm ơn bạn đã sử dụng hệ thống "
                "Rikkei Coffee!"
            )
            break

        case _:
            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 6."
            )