tamp_name = input("Nhập họ và tên bệnh nhân: ")
tamp_age = int(input("Nhập tuổi bệnh nhân: "))
if (tamp_age > 0 and tamp_age < 150) and (tamp_name or not tamp_name == ' ') :
    name = tamp_name
    age = tamp_age
    if (age < 6):
        result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif(age > 80):
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
else:
    result = "LỖI: tên không hợp lệ hoặc tuổi nằm ngoài phạm vi con người (0 - 150)!"

print("===== PHIẾU KHÁM BỆNH =====")
print("Họ tên:", name)
print("Tuổi:", age)
print("Kết quả:", result)