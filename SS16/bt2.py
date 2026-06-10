# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):

    # Tạo bản sao độc lập
    new_prescription = old_prescription.copy()

    # Đổi tên thuốc
    new_prescription[0] = new_prescription[0].replace(
        "Panadol",
        "Paracetamol"
    )

    # Thêm thuốc mới
    new_prescription.append("Oresol")

    return new_prescription


# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)