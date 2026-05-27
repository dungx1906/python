import random
random_number = random.randint(1, 99)

print(random_number)

for i in range(5):
    number_input = int(input("Nhập số bạn chọn: "))
    if(number_input < random_number):
        print("Gợi ý: Số của bạn nhỏ hơn số may mắn!")
    elif(number_input > random_number):
        print("Gợi ý: Số của bạn lớn hơn số may mắn!")
    else:
        print("Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        break

print("--- TRÒ CHƠI KẾT THÚC ---")