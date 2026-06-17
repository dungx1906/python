from datetime import datetime

from colorama import Fore

from utils.score_utils import (
    calculate_average,
    classify_student
)


def display_student_scores(records):

    if not records:
        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )
        return

    print(
        "--- DANH SÁCH ĐIỂM SINH VIÊN ---"
    )

    for index, student in enumerate(
            records,
            start=1):

        average_score = calculate_average(
            student["scores"]
        )

        rank = classify_student(
            average_score
        )

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average_score:.2f} - "
            f"{rank}"
        )

    print("-" * 33)


def export_learning_report(records):

    if not records:
        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )
        return

    total_students = len(records)

    passed_students = 0

    for student in records:

        average_score = calculate_average(
            student["scores"]
        )

        if average_score >= 5:
            passed_students += 1

    failed_students = (
        total_students -
        passed_students
    )

    report_time = datetime.now()

    with open(
            "learning_report.txt",
            "w",
            encoding="utf-8") as report_file:

        report_file.write(
            "BÁO CÁO HỌC TẬP\n"
        )

        report_file.write(
            f"Thời gian: "
            f"{report_time}\n"
        )

        report_file.write(
            f"Tổng sinh viên: "
            f"{total_students}\n"
        )

        report_file.write(
            f"Đạt yêu cầu: "
            f"{passed_students}\n"
        )

        report_file.write(
            f"Cần cải thiện: "
            f"{failed_students}\n"
        )

    print(
        "--- XUẤT BÁO CÁO HỌC TẬP ---"
    )

    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )

    print(
        f"Số sinh viên đạt yêu cầu: "
        f"{passed_students}"
    )

    print(
        f"Số sinh viên cần cải thiện: "
        f"{failed_students}"
    )

    print(
        Fore.GREEN +
        ">> Đã xuất báo cáo ra file "
        "learning_report.txt"
    )