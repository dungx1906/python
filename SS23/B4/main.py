import reports.report_generator as report_module

from data.students import student_records

from utils.string_utils import (
    normalize_student_names
)

from utils.random_utils import (
    generate_assignment_code
)


def main():

    while True:

        print()
        print(
            "===== HỆ THỐNG TIỆN ÍCH "
            "HỌC TẬP RIKKEI ACADEMY ====="
        )

        print(
            "1. Xem danh sách sinh viên "
            "và điểm trung bình"
        )

        print(
            "2. Chuẩn hóa tên sinh viên"
        )

        print(
            "3. Sinh mã bài tập ngẫu nhiên"
        )

        print(
            "4. Xuất báo cáo học tập"
        )

        print(
            "5. Thoát chương trình"
        )

        print("=" * 52)

        try:

            menu_choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if menu_choice == 1:

                report_module.display_student_scores(
                    student_records
                )

            elif menu_choice == 2:

                normalize_student_names(
                    student_records
                )

            elif menu_choice == 3:

                print(
                    "--- SINH MÃ BÀI TẬP ---"
                )

                print(
                    "Mã bài tập của bạn là:",
                    generate_assignment_code()
                )

            elif menu_choice == 4:

                report_module.export_learning_report(
                    student_records
                )

            elif menu_choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )

                break

            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


if __name__ == "__main__":
    main()