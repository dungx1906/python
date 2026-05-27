count = 0
total = 0

for day in range(1, 8):
    revenue = 0
    revenue = int(input(f'Nhập doanh thu Ngày {day}: '))
    total = revenue + total

    if revenue >= 5000000:
        count += 1

print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f'Tổng doanh thu cả tuần: {total} VND')
print(f'Doanh thu trung bình mỗi ngày: {total / 7}')
print(f'Số ngày đạt doanh thu mục tiêu (>= 5.000.000 VND): {count} ngày')