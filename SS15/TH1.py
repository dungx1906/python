inventory_stock = 100
total_revenue = 0.0

menu = """
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
"""

def add_stock(amount) :
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")

def process_sale(quantity):
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Loi: Khong dủ hang trong kho. Ton kho hien tại chỉ con {inventory_stock}.")
        return False
    return True

def calculate_final_price(quantity, price):
    global inventory_stock, total_revenue

    discount = 0
    # - Tính tổng tiền tạm tính = quantity * price.
    total_temp = quantity * price
    # - Nếu tổng tiền ≥ 1000, giảm giá 10% (Tạo biến cục bộ(local) discount trong hàm).
    if total_temp >= 1000:
        discount = total_temp * 0.1  # 10% => tổng / 100 * 10
    # - Cộng thêm 8% thuế VAT vào tổng tiền sau giảm giá.
    # => Tính thêm VAT
    vat = (total_temp - discount) * 0.08
    # - return giá trị tổng tiền cuối cùng (final_total).
    final_total = total_temp - discount + vat

    # - Trừ đi số lượng bán trong inventory_stock.
    inventory_stock -= quantity
    # - Cộng final total vào tổng doanh thu toàn cục (total_revenue).
    total_revenue += final_total
    # - In hóa đơn thành cong ra man hình cho khach hang.
    bill = f"""
-> Hóa đơn chi tiết:
Số lượng: {quantity} | Đơn giá: ${price}
Tạm tính: ${total_temp}
Giảm giá (10%): ${discount}
Thuế VAT (8%): ${vat}
Tổng thanh toán: ${final_total}
Đã bán thanh công!

"""
    print(bill)

def print_report():
    global inventory_stock, total_revenue
    print(f"""
Ton kho hiện tại: {inventory_stock} sản phẩm
Tổng doanh thu: ${total_revenue}1
""")

def number_check(string):
    while True:
        try:
            number = int(input(f"Nhập {string}: "))
        except ValueError:
            print(f"{string} không phải số")
        else:
            if number >= 0:
                print(f"{string} hợp lệ:", number)
                return number
            else:
                print(f"{string} phải lớn hơn 0, vui lòng nhập lại.")

while True:
    print(menu)
    try:
        choice = int(input("Chọn chức năng (1-4): "))
    except ValueError:
        print("Yêu cầu nhập số!")
    else:
        if choice == 1:
            amount = number_check("số lượng sản phẩm muốn thêm")
            add_stock(amount)
            print(f"Tồn kho hiện tại: {inventory_stock}")

        elif choice == 2:
            print(" --- BÁN HÀNG --- ")
            quantity = number_check("số lượng mua ")
            price = float(number_check(" đơn giá ($) "))
            if process_sale(quantity):
                calculate_final_price(quantity, price)

        elif choice == 3:
            print("--- BÁO CÁO KINH DOANH ---")
            print_report()

        elif choice == 4:
            print("Thoát chương trình thành công!")
            break

        else:
            print("Vui lòng chọn đúng chức năng từ 1 - 4!")