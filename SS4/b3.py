quantity = int(input("Nhập số lượng hoá đơn trong ca: "))
max = 0
min = 999999999999999999999999999999999999999

for ordinarily in range(1, quantity + 1):
    number_input = int(input(f'Nhập giá trị hoá đơn thứ {ordinarily}: '))

    if (number_input < min):
        min = number_input

    elif (number_input > max):
        max = number_input


print(f'Hoá đơn có giá trị cao nhất: {max} VND')
print(f'Hoá đơn có giá trị thất nhất: {min} VND')