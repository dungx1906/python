from abc import ABC, abstractmethod

class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @staticmethod
    def validate_account_number(account_number):
        if len(account_number) != 10:
            raise ValueError("Lỗi số tài khoản phải đủ 10 chữ số")

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def with_draw(self, amount): pass

    def __add__(self, other):
        return self.balance + other.balance

    def __lt__(self, other):
        return self.balance < other.balance


class SavingsAccount(BaseAccount):
    def __init__(self, interest_rate):
        super().__init__()

        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount

    def with_draw(self, amount):
        self.__balance -= amount + amount * 0.02

    def apply_interest(self):
        interest = self.__balance * self.interest_rate

        self.__balance += interest


class CreditAccount(BaseAccount):
    def __init__(self, credit_limit):
        super().__init__()

        self.credit_limit = credit_limit

    def with_draw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        pass


class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5000000:
            return amount * 0.01

        return 0


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    def __init__(self, interest_rate):
        super().__init__(interest_rate)


user_1 = BaseAccount()

print(user_1.balance)