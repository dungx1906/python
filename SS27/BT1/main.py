from abc import ABC, abstractmethod


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._BaseAccount__balance = balance

    @property
    def balance(self):
        return self._BaseAccount__balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = " ".join(value.strip().upper().split())

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    def _increase_balance(self, amount):
        self._BaseAccount__balance += amount

    def _decrease_balance(self, amount):
        self._BaseAccount__balance -= amount


class SavingsAccount(BaseAccount):
    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return

        self._increase_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return

        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            print("Số dư không đủ.")
            return

        self._decrease_balance(total)

        print("Rút tiền thành công!")
        print(f"Số tiền rút: {amount:,.0f} VND")
        print(f"Phí phạt rút trước hạn (2%): {fee:,.0f} VND")
        print(f"Số dư còn lại: {self.balance:,.0f} VND")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._increase_balance(interest)

        print(f"Tiền lãi nhận được: +{interest:,.0f} VND")
        print(f"Số dư mới: {self.balance:,.0f} VND")


class CreditAccount(BaseAccount):
    def __init__(self, account_number, owner_name, credit_limit, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return

        self._increase_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return

        if self.balance - amount < -self.credit_limit:
            raise ValueError("Vượt quá hạn mức thấu chi cho phép")

        self._decrease_balance(amount)

        print("Rút tiền thành công! (Sử dụng hạn mức thấu chi)")
        print(f"Số dư hiện tại: {self.balance:,.0f} VND")

class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        return amount * 0.01 if amount > 5_000_000 else 0


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return

        super().deposit(amount)

        cashback = self.cashback_reward(amount)

        if cashback:
            self._increase_balance(cashback)
            print(
                f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% "
                f"({cashback:,.0f} VND)"
            )

        print(f"Số dư mới: {self.balance:,.0f} VND")


class VNPayGateway:
    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống VNPay]: Đang kết nối tới tài khoản "
            f"{account.account_number}..."
        )
        account.withdraw(amount)


class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống Viettel Money]: Đang kết nối tới tài khoản "
            f"{account.account_number}..."
        )
        account.withdraw(amount)


def process_payment(payment_gateway, account, amount):
    try:
        payment_gateway.execute_pay(account, amount)

        print("Xác thực thanh toán bằng Duck Typing thành công!")
        print(
            f"Tài khoản đã thanh toán hóa đơn giá trị: "
            f"{amount:,.0f} VND."
        )
        print(f"Số dư mới: {account.balance:,.0f} VND.")

    except AttributeError:
        print(
            "Cổng thanh toán không hợp lệ "
            "hoặc chưa được tích hợp"
        )

    except Exception as e:
        print("Lỗi:", e)


def display_account(account):
    print("\n--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
    print("Loại tài khoản:", type(account).__name__)
    print("Ngân hàng:", account.bank_name)
    print("Số tài khoản:", account.account_number)
    print("Chủ tài khoản:", account.owner_name)
    print(f"Số dư: {account.balance:,.0f} VND")

    if isinstance(account, (SavingsAccount, HybridAccount)):
        print(f"Lãi suất: {account.interest_rate * 100:.1f}% / năm")

    if isinstance(account, CreditAccount):
        print(f"Hạn mức tín dụng: {account.credit_limit:,.0f} VND")

    print("\n--- MRO ---")
    for cls in account.__class__.mro():
        print(cls.__name__)


def select_account(accounts):
    if not accounts:
        print("Hệ thống chưa có tài khoản.")
        return None

    print("\n--- DANH SÁCH TÀI KHOẢN ---")

    for i, acc in enumerate(accounts, start=1):
        print(
            f"{i}. {acc.account_number} - "
            f"{acc.owner_name} "
            f"({acc.balance:,.0f} VND)"
        )

    try:
        choice = int(input("Chọn tài khoản: "))
        return accounts[choice - 1]
    except:
        print("Lựa chọn không hợp lệ.")
        return None

accounts = []
current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin & Kiểm tra MRO")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Tích lũy / Áp dụng lãi suất")
    print("5. Gộp tài khoản & So sánh")
    print("6. Thanh toán hóa đơn")
    print("7. Thoát chương trình")

    choice = input("Chọn chức năng (1-7): ")

    match choice:

        case "1":
            print("\n--- CHỌN LOẠI TÀI KHOẢN ---")
            print("1. Savings Account\n2. Credit Account\n3. Hybrid Account")

            account_type = input("Chọn loại tài khoản (1-3): ")
            account_number = input("Nhập số tài khoản 10 chữ số: ")

            if not BaseAccount.validate_account_number(account_number):
                print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
                continue

            owner_name = input("Nhập tên chủ tài khoản: ")

            try:
                match account_type:
                    case "1":
                        interest_rate = float(input("Nhập lãi suất năm: "))
                        current_account = SavingsAccount(account_number, owner_name, interest_rate, 10_000_000)
                        print("\nMở tài khoản Tiết kiệm thành công!")

                    case "2":
                        credit_limit = float(input("Nhập hạn mức tín dụng: "))
                        current_account = CreditAccount(account_number, owner_name, credit_limit)
                        print("\nMở tài khoản Tín dụng thành công!")

                    case "3":
                        interest_rate = float(input("Nhập lãi suất năm: "))
                        current_account = HybridAccount(account_number, owner_name, interest_rate, 10_000_000)
                        print("\nMở tài khoản Hybrid thành công!")

                    case _:
                        print("Loại tài khoản không hợp lệ.")
                        continue

                accounts.append(current_account)
                print("Chủ tài khoản:", current_account.owner_name)

            except Exception as e:
                print("Lỗi:", e)

        case "2":
            if not current_account:
                print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản trước.")
                continue

            display_account(current_account)

        case "3":
            if not current_account:
                print("Chưa có tài khoản được chọn.")
                continue

            print("\n1. Nạp tiền\n2. Rút tiền")
            action = input("Chọn giao dịch (1-2): ")

            try:
                amount = float(input("Nhập số tiền: ").replace(",", ""))

                match action:
                    case "1":
                        current_account.deposit(amount)

                    case "2":
                        current_account.withdraw(amount)

                    case _:
                        print("Lựa chọn không hợp lệ.")

            except Exception as e:
                print("Lỗi:", e)

        case "4":
            if not current_account:
                print("Chưa có tài khoản.")
                continue

            if isinstance(current_account, (SavingsAccount, HybridAccount)):
                print("\n--- TÍNH LÃI ĐỊNH KỲ ---")
                print(f"Số dư trước tính lãi: {current_account.balance:,.0f} VND")
                print(f"Lãi suất năm: {current_account.interest_rate * 100:.1f}%")
                current_account.apply_interest()
            else:
                print("Tài khoản tín dụng không hỗ trợ tính lãi tiết kiệm.")

        case "5":
            if len(accounts) < 2:
                print("Cần ít nhất 2 tài khoản.")
                continue

            print(f"\nTài khoản A: {current_account.owner_name} ({current_account.balance:,.0f} VND)")

            other_account = select_account(accounts)

            if not other_account or other_account == current_account:
                print("Tài khoản đối ứng không hợp lệ.")
                continue

            try:
                print("[Kết quả So sánh (__lt__)]:", "A nhỏ hơn B" if current_account < other_account else "A không nhỏ hơn B")
                print(f"[Kết quả Tổng hợp (__add__)]: {(current_account + other_account):,.0f} VND")

            except TypeError:
                print("Không thể so sánh tài khoản.")

        case "6":
            if not current_account:
                print("Chưa có tài khoản.")
                continue

            print("\n1. VNPay\n2. Viettel Money")

            gateway_choice = input("Chọn cổng thanh toán (1-2): ")

            try:
                amount = float(input("Nhập số tiền hóa đơn: ").replace(",", ""))

                match gateway_choice:
                    case "1":
                        gateway = VNPayGateway()

                    case "2":
                        gateway = ViettelMoneyGateway()

                    case _:
                        print("Cổng thanh toán không hợp lệ.")
                        continue

                process_payment(gateway, current_account, amount)

            except Exception as e:
                print("Lỗi:", e)

        case "7":
            print("\nCảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!")
            break

        case _:
            print("Vui lòng chọn từ 1 đến 7.")