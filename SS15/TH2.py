atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(
        f"Tài khoản của bạn: "
        f"{user_account_balance:,} VND"
    )
    print(
        f"(Debug) Tiền mặt trong ATM: "
        f"{atm_vault_balance:,} VND"
    )

def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance
    if amount <= 0:
        return False
    user_account_balance += amount
    atm_vault_balance += amount
    return True

def check_withdrawal_rules(amount):
    fee = 1100
    if amount <= 0:
        return "INVALID_AMOUNT"
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"
    total_deduction = amount + fee
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"

def execute_withdrawal(
        total_deduction,
        amount_to_dispense):
    global user_account_balance
    global atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(
        f"Bạn đã rút thành công "
        f"{amount_to_dispense:,} VND."
    )
    print(
        f"Số dư tài khoản còn lại: "
        f"{user_account_balance:,} VND."
    )

while True:

    print("""
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
""")

    try:
        choice = int(
            input(
                "Vui lòng chọn giao dịch (1-4): "
            )
        )
    except ValueError:
        print("Lựa chọn không hợp lệ!")
        continue
    if choice == 1:
        display_balances()

    elif choice == 2:
        print("\n--- NẠP TIỀN ---")
        try:
            amount = int(
                input(
                    "Nhập số tiền muốn nạp: "
                )
            )
        except ValueError:
            print("Số tiền không hợp lệ")
            continue
        if deposit_money(amount):
            print(
                "Giao dịch thành công! "
                f"Số dư tài khoản hiện tại: "
                f"{user_account_balance:,} VND."
            )
        else:
            print("Số tiền không hợp lệ")

    elif choice == 3:
        print("\n--- RÚT TIỀN ---")
        try:
            amount = int(
                input(
                    "Nhập số tiền cần rút: "
                )
            )
        except ValueError:
            print("Số tiền không hợp lệ")
            continue
        status = check_withdrawal_rules(
            amount
        )
        if status == "INVALID_AMOUNT":
            print(
                "Số tiền không hợp lệ"
            )
        elif status == "INVALID_MULTIPLE":
            print(
                "Số tiền rút phải là "
                "bội số của 50,000"
            )
        elif status == "INSUFFICIENT_FUNDS":
            print(
                "Giao dịch thất bại: "
                "Tài khoản không đủ tiền."
            )
        elif status == "ATM_OUT_OF_CASH":
            print(
                "Giao dịch thất bại: "
                "Máy ATM không đủ tiền mặt "
                "để phục vụ."
            )
        else:
            fee = 1100
            total_deduction = (
                amount + fee
            )
            execute_withdrawal(
                total_deduction,
                amount
            )

    elif choice == 4:
        print(
            "Cảm ơn quý khách đã sử dụng dịch vụ!"
        )
        break
    else:
        print(
            "Lựa chọn không hợp lệ!"
        )
