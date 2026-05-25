print("===== KIOSK KHÁM BỆNH TỰ ĐỘNG =====")
patient_name = input("Nhập họ tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh nhân: ")
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
heart_rate = int(input("Nhập nhịp tim (bpm): "))
weight = float(input("Nhập cân nặng (kg): "))
print("==============================")
print("   PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("==============================")

print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Mã bệnh nhân     : {patient_id}")

print("--- CHỈ SỐ SINH HIỆU ---")
print(f"Nhiệt độ         : {temperature} °C")
print(f"Nhịp tim         : {heart_rate} bpm")
print(f"Cân nặng         : {weight} kg")

print("==============================")
print("      HOÀN TẤT TIẾP NHẬN")
print("==============================")
print("\n========== SYSTEM LOG ==========")

print(f"patient_name -> {patient_name} | Kiểu dữ liệu: {type(patient_name)}")
print(f"patient_id   -> {patient_id} | Kiểu dữ liệu: {type(patient_id)}")

print(f"temperature  -> {temperature} | Kiểu dữ liệu: {type(temperature)}")
print(f"heart_rate   -> {heart_rate} | Kiểu dữ liệu: {type(heart_rate)}")
print(f"weight       -> {weight} | Kiểu dữ liệu: {type(weight)}")

print("================================")