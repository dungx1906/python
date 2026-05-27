is_correct = False

while not is_correct:
    total = int(input("Nhập tổng tiền ban đầu: "))
    if total > 0:
        is_correct = True
    else:
        print("Nhập sai giá cả là số âm, vui lòng nhập lại")

if total >500000:
    total = total * 0.1
    print(f'Số tiền được giảm giá: {total} VND')
    print(f'Số tiền phải trả: {total * 9}')
else:
    print(f'Nhập số tiền phải trả là: {total}')