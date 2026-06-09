def number_check():
    while True:
        number = int(input("Nhập số: "))
        if number > 0:
            print("Số hợp lệ:", number)
            return number
        else:
            print("Số phải lớn hơn 0, vui lòng nhập lại.")

number1 = number_check()