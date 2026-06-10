from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()
    for index, record in enumerate(records):
        if record.startswith(patient_id + "-"):
            return index
    return -1

def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    for index, record in enumerate(records, 1):
        patient_id, name, birth_year, diagnosis = record.split("-")
        print(
            f"{index}. [{patient_id}] "
            f"{name:<18} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )
    print("--------------------------------------------------------------------------")

def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()
    name = name.replace("-", " ").title()
    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()
        if birth_year.isdigit():
            birth_year = int(birth_year)
            if 1900 <= birth_year <= current_year:
                break

        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ").strip()
    diagnosis = diagnosis.replace("-", " ").capitalize()
    record = "-".join(
        [
            patient_id,
            name,
            str(birth_year),
            diagnosis
        ]
    )
    records.append(record)
    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu là:")
    print(record)

def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()
    index = find_patient_index(records, patient_id)
    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    patient_info = records[index].split("-")
    print(f"\nTìm thấy bệnh nhân: {patient_info[1]}")
    print(f"Chẩn đoán hiện tại: {patient_info[3]}")
    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip()
    new_diagnosis = (
        new_diagnosis
        .replace("-", " ")
        .capitalize()
    )
    patient_info[3] = new_diagnosis
    updated_record = "-".join(patient_info)
    records[index] = updated_record
    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(updated_record)

def generate_age_report(records):
    current_year = datetime.now().year
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        patient_info = record.split("-")
        birth_year = int(patient_info[2])
        age = current_year - birth_year
        if age < 16:
            children += 1

        elif age <= 60:
            adults += 1

        else:
            elderly += 1
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        display_records(patient_records)

    elif choice == "2":
        add_patient(patient_records)

    elif choice == "3":
        update_diagnosis(patient_records)

    elif choice == "4":
        generate_age_report(patient_records)

    elif choice == "5":
        print("\nCảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("\nLựa chọn không hợp lệ!")