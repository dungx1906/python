import logging

logging.basicConfig(
    filename= "output.log",
    filemode= "a",
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    # datefmt= "%y-%m-%d %h-%m-%s",
    encoding= "utf-8"
)

balance = 500

while True:
    try:
        amount = int(input("Nhập vào vào số tiền: "))

    except ValueError:
        print("Vui lòng nhập vào số tiền hợp lệ")

    else:
        if amount <= 0:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0")
        else:
            break

balance += amount

logging.info(f"Deposit successful: {amount} VND. Current Balance: {balance}")
logging.error(f"InvalidAmountError: Attempted to process -100000 VND.")

