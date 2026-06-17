from datetime import datetime

from utils.file_helper import create_log_directory
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta


shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]


print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS ======")

create_log_directory("logs")

print(
    "[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công."
)

print("-" * 75)

for shipment in shipments:

    shipment_id = shipment["id"]

    distance_km = calculate_distance(
        shipment["from_lat"],
        shipment["from_lon"],
        shipment["to_lat"],
        shipment["to_lon"]
    )

    estimated_arrival_time = predict_eta(
        shipment["depart"],
        distance_km
    )

    delivery_deadline = datetime.strptime(
        shipment["deadline"],
        "%Y-%m-%d %H:%M:%S"
    )

    print(f"[CHUYẾN XE {shipment_id}]")

    print(
        f" + Khoảng cách vận chuyển: {distance_km:.2f} km"
    )

    print(
        f" + Thời gian khởi hành: {shipment['depart']}"
    )

    print(
        " + Dự kiến cập bến (ETA): "
        f"{estimated_arrival_time.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    if estimated_arrival_time <= delivery_deadline:
        print(
            " + Trạng thái: 🟢 AN TOÀN "
            "(Kịp tiến độ trước deadline)"
        )
    else:
        print(
            " + Trạng thái: 🔴 CẢNH BÁO "
            f"(Trễ hạn! Deadline yêu cầu lúc "
            f"{delivery_deadline.strftime('%H:%M:%S')})"
        )

    log_file_path = f"logs/{shipment_id}.log"

    with open(
            log_file_path,
            "w",
            encoding="utf-8") as log_file:

        log_file.write(
            f"Ma chuyen xe: {shipment_id}\n"
        )

        log_file.write(
            f"Khoang cach: {distance_km:.2f} km\n"
        )

        log_file.write(
            f"Khoi hanh: {shipment['depart']}\n"
        )

        log_file.write(
            f"ETA: "
            f"{estimated_arrival_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        if estimated_arrival_time <= delivery_deadline:
            log_file.write(
                "Trang thai: AN TOAN\n"
            )
        else:
            log_file.write(
                "Trang thai: TRE HAN\n"
            )

    print()

print("=" * 55)