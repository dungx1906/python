class CoffeeOrder:

    # Class Attribute
    vat_rate = 0.10

    def __init__(self, table_number):

        self.table_number = table_number

        # Private Attribute
        self.__total_amount = 0

    def add_item(self, price):

        if price > 0:
            self.__total_amount += price

    @property
    def total_amount(self):

        return self.__total_amount

    def calculate_final_bill(self):

        return (
            self.__total_amount
            + self.__total_amount * CoffeeOrder.vat_rate
        )

    @classmethod
    def update_vat_rate(cls, new_rate):

        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate


order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

print("=== TRƯỚC KHI ĐỔI VAT ===")

print(
    f"Bàn 1: {order_table1.total_amount} VNĐ"
)

print(
    f"Bàn 2: {order_table2.total_amount} VNĐ"
)

# Thử gian lận

try:

    order_table1.total_amount = 0

except AttributeError:

    print(
        "Không thể sửa trực tiếp "
        "total_amount!"
    )

# Cập nhật VAT cho toàn hệ thống

CoffeeOrder.update_vat_rate(0.08)

print("\n=== SAU KHI ĐỔI VAT ===")

print(
    f"VAT Bàn 1: "
    f"{order_table1.vat_rate}"
)

print(
    f"VAT Bàn 2: "
    f"{order_table2.vat_rate}"
)

print(
    f"Tổng tiền Bàn 1: "
    f"{order_table1.calculate_final_bill():,.0f} VNĐ"
)

print(
    f"Tổng tiền Bàn 2: "
    f"{order_table2.calculate_final_bill():,.0f} VNĐ"
)