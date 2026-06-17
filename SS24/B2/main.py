class MemberCard:

    def __init__(self, customer_name, points=0):

        self.customer_name = customer_name

        self.__points = 0

        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):

        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):

        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng thêm không hợp lệ!")

    @staticmethod
    def is_eligible_for_voucher(bill_amount):

        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

print("=== TRƯỚC KHI GÁN SAI ===")
print(
    f"Khách hàng: {card1.customer_name}"
)
print(
    f"Điểm hiện tại: {card1.points}"
)

print("\n=== THỬ GÁN ĐIỂM ÂM ===")

card1.points = -50

print(
    f"Điểm sau khi gán: {card1.points}"
)

print("\n=== THỬ GÁN CHUỖI ===")

card1.points = "một trăm"

print(
    f"Điểm sau khi gán: {card1.points}"
)

print("\n=== KIỂM TRA VOUCHER ===")

result = MemberCard.is_eligible_for_voucher(
    250000
)

print(
    f"Hóa đơn 250000 VNĐ "
    f"được tặng Voucher: {result}"
)