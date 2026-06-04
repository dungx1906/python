cart_items = [
         {
         	"id": "P001",
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon",
         	"number": 2,
         	"price": 150000
         }
]

# In tiêu đề
print("--- CHI TIẾT GIỎ HÀNG ---")

# Định nghĩa Header và căn lề (< là căn trái, số là độ rộng của cột)
header = f"{'STT':<3} | {'Mã SP':<6} | {'Tên Sản Phẩm':<22} | {'SL':<2} | {'Đơn Giá':<12} | {'Thành Tiền':<12}"
print(header)

# In đường kẻ ngang (độ dài bằng đúng độ dài của header)
print("-" * len(header))

total_product = 0
total_money = 0

# Duyệt qua từng sản phẩm và in ra
for i, sp in enumerate(cart_items, start = 1):
    thanh_tien = sp["number"] * sp["price"]

    # Định dạng từng dòng với độ rộng cột tương ứng với header
    row = (
        f"{i:<3} | "
        f"{sp["id"]:<6} | "
        f"{sp["name"]:<22} | "
        f"{sp["number"]:<2} | "
        f"{(sp["price"]):<12} | "
        f"{(thanh_tien):<12}"
    )

    total_product += sp["number"]
    total_money += thanh_tien

    print(row)

# In đường kẻ ngang chốt lại bảng
print("-" * len(header))

print(f"Tổng số lượng sản phẩm trong giỏ: {total_product}")
print(f"TỔNG TIỀN THANH TOÁN {total_money:,}đ")
