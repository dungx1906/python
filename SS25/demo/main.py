class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        self.__account_name = new_name.strip().upper()



user_account = BankAccount("0774122999", "Dương Trung Dũng")
print(user_account.account_number)
print(user_account.account_name)
print(user_account.balance)
print(user_account.bank_name)
print(user_account.transaction_fee)