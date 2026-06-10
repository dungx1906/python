raw_logs = []
processed_logs = []

def clean_logs(raw_text):
    translation_table = str.maketrans("", "", "!@#$")
    cleaned_text = raw_text.translate(
        translation_table
    )

    logs = [
        log.strip()
        for log in cleaned_text.split(";")
        if log.strip()
    ]
    return logs

def load_logs():
    global raw_logs
    print("\n--- NẠP DỮ LIỆU LOG ---")
    raw_input_log = input(
        "Nhập chuỗi log thô (cách nhau bởi dấu ;): "
    )

    raw_logs = clean_logs(raw_input_log)
    print(
        f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống."
    )

def filter_danger_logs():
    global processed_logs
    if len(raw_logs) == 0:
        print(
            "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
        )
        return

    print("\n--- LỌC CẢNH BÁO ---")
    processed_logs = [
        log
        for log in raw_logs
        if "error" in log.lower()
        or "critical" in log.lower()
    ]
    print(
        f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:"
    )
    for log in processed_logs:
        print(f"- {log}")

def mask_single_ip(ip_address):
    parts = ip_address.split(".")
    if len(parts) == 4:
        parts[2] = "*"
        parts[3] = "*"
        return ".".join(parts)
    return ip_address

def mask_ip_logs():
    if len(raw_logs) == 0:
        print(
            "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
        )
        return

    if len(processed_logs) == 0:
        print(
            "Chưa có log cảnh báo, vui lòng thực hiện chức năng 2"
        )
        return
    print("\n--- MÃ HÓA IP ---")
    safe_logs = []

    for log in processed_logs:
        words = log.split()
        new_words = []
        for word in words:
            if "." in word:
                word = mask_single_ip(word)
            new_words.append(word)
        safe_logs.append(
            " ".join(new_words)
        )
    print("Báo cáo log an toàn:")
    for index, log in enumerate(safe_logs, 1):
        print(f"{index}. {log}")
    return safe_logs

while True:
    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")

    choice = input(
        "Chọn chức năng (1-4): "
    ).strip()
    if choice == "1":
        load_logs()

    elif choice == "2":
        filter_danger_logs()

    elif choice == "3":
        mask_ip_logs()

    elif choice == "4":
        print(
            "\nĐóng hệ thống Security Log Analyzer..."
        )
        break

    else:
        print(
            "Lựa chọn không hợp lệ!"
        )