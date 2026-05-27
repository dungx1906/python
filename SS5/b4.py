branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")

    for classroom in range(1, class_count + 1):

        while True:
            student_count = int(input(f"Nhập số học viên đi học lớp {classroom}: "))
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")

            elif student_count == 0:
                print(
                    f"Chi nhánh {branch} - Lớp {classroom}: "
                    "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
                )
                break

            elif student_count >= 20:
                print(
                    f"Chi nhánh {branch} - Lớp {classroom}: "
                    "Lớp học ổn định"
                )
                break
            else:
                print(
                    f"Chi nhánh {branch} - Lớp {classroom}: "
                    "Lớp cần được nhắc nhở và theo dõi"
                )
                break
