class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__balance = 0
        self.__account_name = ""
        self.account_name = account_name

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        cleaned_name = " ".join(new_name.strip().split())

        if not cleaned_name:
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = cleaned_name.upper()

    @property
    def account_number(self):
        return self.__account_number

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return False

        cls.transaction_fee = new_fee
        return True

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        if self.__balance < amount + BankAccount.transaction_fee:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False

        self.__balance -= amount + BankAccount.transaction_fee
        return True

    def display_info(self):
        print(
            f"\n--- THÔNG TIN TÀI KHOẢN ---"
            f"\nNgân hàng: {BankAccount.bank_name}"
            f"\nSố tài khoản: {self.__account_number}"
            f"\nTên chủ tài khoản: {self.__account_name}"
            f"\nSố dư hiện tại: {self.__balance:,} VND"
            f"\nPhí giao dịch: {BankAccount.transaction_fee:,} VND"
        )


current_account = None

while True:
    print("""
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================
""")

    choice = input("Chọn chức năng (1-6): ")

    match choice:

        case "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")

            while True:
                account_number = input("Nhập số tài khoản 10 chữ số: ")

                if BankAccount.validate_account_number(account_number):
                    break

                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            account_name = input("Nhập tên chủ tài khoản: ")
            current_account = BankAccount(account_number, account_name)

            print(
                f"Mở tài khoản thành công!"
                f"\nSố tài khoản: {current_account.account_number}"
                f"\nTên chủ tài khoản: {current_account.account_name}"
            )

        case "2":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản\nVui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                current_account.display_info()

        case "3":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản\nVui lòng mở tài khoản ở Chức năng 1 trước.")
                continue

            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---\n1. Nạp tiền\n2. Rút tiền")
            transaction_choice = input("Chọn loại giao dịch (1-2): ")

            try:
                amount = int(input("Nhập số tiền giao dịch: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
                continue

            match transaction_choice:

                case "1":
                    if current_account.deposit(amount):
                        print(
                            f"Nạp tiền thành công: +{amount:,} VND"
                            f"\nSố dư mới: {current_account.balance:,} VND"
                        )

                case "2":
                    if current_account.withdraw(amount):
                        print(
                            f"Rút tiền thành công: -{amount:,} VND"
                            f"\nPhí giao dịch: {BankAccount.transaction_fee:,} VND"
                            f"\nSố dư mới: {current_account.balance:,} VND"
                        )
                    else:
                        print(f"Số dư mới: {current_account.balance:,} VND")

                case _:
                    print("Lựa chọn không hợp lệ.")

        case "4":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản\nVui lòng mở tài khoản ở Chức năng 1 trước.")
                continue

            print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

            old_name = current_account.account_name
            current_account.account_name = input("Nhập tên mới: ")

            if old_name != current_account.account_name:
                print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        case "5":
            print(
                f"\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
                f"\nPhí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND"
            )

            try:
                new_fee = int(input("Nhập phí giao dịch mới: "))

                if BankAccount.update_transaction_fee(new_fee):
                    print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND")
                else:
                    print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND")

            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        case "6":
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        case _:
            print("Lựa chọn không hợp lệ.")