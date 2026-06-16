import logging

logging.basicConfig(
    filename= "momo_transactions.log",
    filemode= "a",
    level= logging.INFO,
    format= "%(asctime)s - %(message)s",
    # datefmt= "%y-%m-%d %h-%m-%s",
    encoding= "utf-8"
)
balance = 0

menu = """
========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3.  Xem số dư hiện tại
4. Thoát chương trình 
===============================================
"""

def recharge(urse_balance):
    try:
        amount = int(input("Nhập vào vào số tiền: "))

    except ValueError:
        print("Vui lòng nhập vào số tiền hợp lệ")
        logging.error(f"- ERROR - ValueError: Invalid numeric input for deposit.")

    else:
        if amount <= 0:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0")
            logging.error(f"- ERROR - InvalidAmountError: Attempted to process -100000 VND.")
        else:
            urse_balance += amount

            logging.info(f"[INFO] - Deposit successful: +{amount} VND. Current Balance: {urse_balance}.")
            print(f"Nạp tiền thành công +{[amount]:,} VND, tài khoản {[urse_balance]:,} VND")
            return urse_balance

def Transfer(urse_balance):
    try:
        amount_transferred = int(input("Nhập vào số tiền cần chuyển: "))

    except ValueError:
        print("Vui lòng nhập số!")

    else:
        if amount_transferred > urse_balance:
            print("Giao dịch thất bại: Số dư của bạn không đủ")
            print(f"Số dư hiện tại: {urse_balance:,}")
            logging.error(
                f"ERROR - InsufficientBalanceError: Attempted to transfer {amount_transferred} VND with {urse_balance} 300000 VND.")

        elif amount_transferred >= 10000000:
            urse_balance = urse_balance - amount_transferred
            print(f"Số tiền đã chuyển: {amount_transferred:,} VND")
            print(f"Số dư còn lại: {urse_balance:,} VND")
            logging.warning(f"WARNING - High value transaction detected: {amount_transferred} VND to {number_phone}")

        elif amount_transferred <= 0:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0")
            logging.error(f"ERROR - InvalidAmountError: Attempted to process -{amount_transferred} VND.")

        else:
            urse_balance = urse_balance - amount_transferred
            print(f"Chuyển tiền thành công tới số điện thoại {number_phone}")
            print(f"Số tiền đã chuyển: {amount_transferred:,} VND")
            print(f"Số dư còn lại: {urse_balance:,} VND")
            logging.info(
                f"INFO - Transfer successful: -{amount_transferred} VND to 0987654321. Current Balance: {urse_balance}")

while True:
    print(menu)

    try:
        choice = int(input("Chọn chức năng (1-4):"))

    except ValueError:
        print("Vui lòng nhập vào số!")

    else:
        match choice:
            case 1:
                print("Chức năng 1")
                balance = recharge(balance)

            case 2:
                print("Chức năng 2")

                while True:
                    number_phone = str(input("Nhập vào số điện thoại (0xxxxxxxxx): "))

                    if not number_phone.isdigit():
                        print("Vui lòng nhập số!")

                    elif len(number_phone) != 10 or number_phone[0] != 0:
                        print("Vui lòng nhập đúng định đạng")

                    else:
                        break

                    Transfer(balance)

            case 3:
                print("Chức năng 3")
                print(f"Số dư hiện tại; {balance:,}")

            case 4:
                print("Thoát chương trình")
                break

            case _:
                print("Vui lòng chọn chức năng (1-4)!")



