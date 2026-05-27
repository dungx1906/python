branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
report = ""

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(
            input(f'Nhập doanh thu Chi nhánh {branch}, thang {month}:')
        )
        result = f"Chi nhánh {branch}, thắng {month}: {revenue} triệu đồng\n"
        report += result

print("-------------- Kết quả --------------")
print(report)