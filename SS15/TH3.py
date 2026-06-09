available_seats = 50
flight_revenue = 0.0

BASE_PRICE = 2000.0
MAX_CAPACITY = 50

def calculate_ticket_cost(quantity, ticket_class):
    if ticket_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5
    subtotal = quantity * ticket_price
    service_fee = subtotal * 0.05
    total_payment = subtotal + service_fee
    return total_payment

def book_ticket(quantity, total_payment):
    global available_seats
    global flight_revenue
    if quantity > available_seats:
        return False
    available_seats -= quantity
    flight_revenue += total_payment
    return True

def cancel_ticket(quantity):
    global available_seats
    global flight_revenue
    if available_seats + quantity > MAX_CAPACITY:
        return -1
    refund_amount = quantity * BASE_PRICE * 0.8
    available_seats += quantity
    flight_revenue -= refund_amount
    return refund_amount

def display_flight_status():
    booked_seats = MAX_CAPACITY - available_seats
    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:.2f}")

while True:

    print("""
============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================
""")

    try:
        choice = int(input("Chọn chức năng (1-4): "))
    except ValueError:
        print("Lựa chọn không hợp lệ!")
        continue

    if choice == 1:
        print("\n--- ĐẶT VÉ MÁY BAY ---")
        try:
            quantity = int(input("Nhập số lượng vé: "))
        except ValueError:
            print("Số lượng vé không hợp lệ.")
            continue
        if quantity <= 0:
            print("Số lượng vé phải lớn hơn 0.")
            continue
        try:
            ticket_class = int(
                input(
                    "Chọn hạng vé (1: Economy, 2: Business): "
                )
            )
        except ValueError:
            print("Hạng vé không hợp lệ.")
            continue

        if ticket_class not in [1, 2]:
            print("Hạng vé không hợp lệ.")
            continue

        if quantity > available_seats:
            print(
                f"Rất tiếc, chuyến bay chỉ còn "
                f"{available_seats} chỗ trống."
            )
            continue

        total_payment = calculate_ticket_cost(
            quantity,
            ticket_class
        )

        if ticket_class == 1:
            class_name = "Economy"
            ticket_price = BASE_PRICE
        else:
            class_name = "Business"
            ticket_price = BASE_PRICE * 1.5

        subtotal = quantity * ticket_price
        service_fee = subtotal * 0.05
        book_ticket(quantity, total_payment)
        print("\n-> Xác nhận đặt chỗ:")
        print(
            f"Số lượng: {quantity} | "
            f"Hạng: {class_name}"
        )
        print(f"Tạm tính: ${subtotal:.2f}")
        print(f"Phí dịch vụ (5%): ${service_fee:.2f}")
        print(f"Tổng thanh toán: ${total_payment:.2f}")
        print(
            f"Đặt vé thành công! "
            f"Ghế trống còn lại: {available_seats}"
        )

    elif choice == 2:
        print("\n--- HỦY VÉ & HOÀN TIỀN ---")
        try:
            quantity = int(
                input(
                    "Nhập số lượng vé muốn hủy: "
                )
            )
        except ValueError:
            print("Số lượng vé không hợp lệ.")
            continue
        if quantity <= 0:
            print("Số lượng vé không hợp lệ.")
            continue
        refund_amount = cancel_ticket(quantity)
        if refund_amount == -1:
            print(
                "Lỗi: Số lượng vé hủy vượt quá "
                "số vé đã bán ra."
            )
        else:
            print(
                f"Hủy vé thành công. "
                f"Hệ thống đã hoàn lại: "
                f"${refund_amount:.2f} "
                f"(80% giá cơ bản)."
            )
            print(
                f"Ghế trống hiện tại: "
                f"{available_seats}"
            )

    elif choice == 3:
        display_flight_status()

    elif choice == 4:
        print(
            "Cảm ơn quý khách đã sử dụng dịch vụ!"
        )
        break

    else:

        print("Lựa chọn không hợp lệ!")