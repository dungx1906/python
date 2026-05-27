
is_correct = False

while not is_correct:
    classroom = int(input("Nhập số phòng học: "))
    col = int(input("Nhập số hàng ghế: "))
    row = int(input("Nhập số ghế trên mỗi hàng: "))

    if classroom > 0:
        if col > 0 and row > 0:
            if col < 10 and row < 10:
                print("Phòng học hợp lệ.")
                is_correct = True
            else:
                print("Phòng quá lớn. Đừng nhập dữ liệu!")

        else:
            print("Dữ liệu phòng họp không hợp lệ. Bỏ qua phòng họp này")

    else:
        print("Số lượng phòng học không hợp lệ!")

for i in range(1, classroom + 1):
    print(f'Phòng học {i}')
    for J in range(1,col + 1):
        for l in range(1, row + 1):
            print("*", end = " ")
        print("\n")
    print("-------------------------------")

