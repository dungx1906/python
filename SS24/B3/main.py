class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = " ".join(name.split()).title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):
        earned_points = bill_amount // 10000
        self.__points += earned_points

        upgraded = False
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            upgraded = True

        return earned_points, upgraded

    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            return None

        self.__points -= points_to_use
        discount_amount = points_to_use * MemberCard.point_value_vnd
        return discount_amount

    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):
        return (
            len(card_id) == 4
            and card_id.startswith("RC")
            and card_id[2:].isdigit()
        )


cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]

cards_database[0].earn_points(1500000)  # 150 điểm => VIP
cards_database[1].earn_points(200000)   # 20 điểm


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")

    try:
        choice = int(input("Chọn chức năng (1-6): "))

        match choice:

            case 1:
                print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

                if not cards_database:
                    print("Chưa có dữ liệu thẻ.")
                else:
                    for index, card in enumerate(cards_database, start=1):
                        print(
                            f"{index}. Mã: {card.card_id} | "
                            f"Tên: {card.name} | "
                            f"Điểm: {card.points} | "
                            f"Hạng: {card.tier}"
                        )

            case 2:
                print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

                card_id = input("Nhập mã thẻ: ").strip()

                if not MemberCard.is_valid_card_id(card_id):
                    print("Mã thẻ không hợp lệ!")
                    continue

                if find_card(card_id):
                    print("Mã thẻ đã tồn tại trong hệ thống!")
                    print("Vui lòng kiểm tra lại.")
                    continue

                customer_name = input("Nhập tên khách hàng: ")

                new_card = MemberCard(card_id, customer_name)
                cards_database.append(new_card)

                print("\nĐăng ký thẻ thành viên thành công!")
                print(f"Mã thẻ: {new_card.card_id}")
                print(f"Tên khách hàng: {new_card.name}")
                print(f"Điểm ban đầu: {new_card.points}")
                print(f"Hạng thẻ: {new_card.tier}")

            case 3:
                print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

                card_id = input("Nhập mã thẻ: ").strip()

                card = find_card(card_id)

                if not card:
                    print("Không tìm thấy thẻ!")
                    continue

                try:
                    bill_amount = int(
                        input("Nhập tổng tiền hóa đơn: ")
                    )

                    earned_points, upgraded = card.earn_points(
                        bill_amount
                    )

                    print(f"\nKhách hàng: {card.name}")
                    print(f"Hóa đơn: {bill_amount:,} VNĐ")
                    print(f"Số điểm được tích: {earned_points}")
                    print(f"Tổng điểm hiện tại: {card.points}")

                    if upgraded:
                        print(
                            "Chúc mừng! Khách hàng đã được nâng hạng VIP."
                        )

                    print(f"Hạng thẻ hiện tại: {card.tier}")

                except ValueError:
                    print("Tổng tiền phải là số nguyên!")

            case 4:
                print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

                card_id = input("Nhập mã thẻ: ").strip()

                card = find_card(card_id)

                if not card:
                    print("Không tìm thấy thẻ!")
                    continue

                try:
                    points_to_use = int(
                        input("Nhập số điểm muốn sử dụng: ")
                    )

                    discount_amount = card.redeem_points(
                        points_to_use
                    )

                    if discount_amount is None:
                        print("\nKhông thể đổi điểm!")
                        print(
                            "Số điểm muốn sử dụng vượt quá "
                            "số điểm hiện có."
                        )
                        print(
                            f"Điểm hiện tại của khách: "
                            f"{card.points}"
                        )
                        print(
                            f"Số điểm sau giao dịch: "
                            f"{card.points}"
                        )
                    else:
                        print(f"\nĐã trừ {points_to_use} điểm.")
                        print(
                            f"Khách hàng được giảm giá "
                            f"{discount_amount:,} VNĐ vào hóa đơn!"
                        )
                        print(
                            f"Số điểm còn lại: "
                            f"{card.points}"
                        )
                        print(
                            f"Hạng thẻ hiện tại: "
                            f"{card.tier}"
                        )

                except ValueError:
                    print("Điểm sử dụng phải là số nguyên!")

            case 5:
                print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

                print(
                    f"Tỷ giá hiện tại: "
                    f"1 điểm = "
                    f"{MemberCard.point_value_vnd:,} VNĐ"
                )

                try:
                    new_value = int(
                        input(
                            "Nhập tỷ giá mới cho 1 điểm: "
                        )
                    )

                    MemberCard.update_point_value(
                        new_value
                    )

                    print("Cập nhật tỷ giá thành công!")
                    print(
                        f"Tỷ giá mới: "
                        f"1 điểm = "
                        f"{MemberCard.point_value_vnd:,} VNĐ"
                    )

                except ValueError:
                    print("Tỷ giá phải là số nguyên!")

            case 6:
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống "
                    "thẻ thành viên Rikkei Coffee!"
                )
                break

            case _:
                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 6."
                )

    except ValueError:
        print("Vui lòng nhập một số từ 1 đến 6.")