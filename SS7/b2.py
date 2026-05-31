transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()
amount = parts[2].strip()
status = parts[3].strip().upper()

print("Hoc vien:", student_name)
print("Khoa hoc:", course_code)
print("So tien:", amount, "VND")
print("Trang thai:", status)