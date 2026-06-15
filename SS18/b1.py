orders = [

    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 105000000, 'status': 'Paid'},

    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Paid'}

]
while True:
    choice = input('''
======================================
    QUAN LI DON HANG - AGENT ORDER
======================================
1. Xem danh sách đơn hàng hiện có
2. Tạo mới đơn hàng đại lý
3. Cập nhập trạng thái thanh toán
4. Tính tổng doanh thu & chiết khấu
5. Thoát chương trình
======================================
Chọn chức năng (1-5): ''')

    match choice:
        case "1":
            if len(orders) == 0:
                print('Hệ thống hiện không có đơn hàng nào!')
            else:
                print('-- DANH SÁCH ĐƠN HÀNG ĐẠI LÝ --')
                header = f'{'Mã Đơn':<7} | {'Tên Đại Lý':<20} | {'Giá trị (VNĐ)':<15} | {"Trạng thái":<10}'
                print(header)
                print('-'* len(header))
                for value in orders:
                    print(f'{value["id"]:<7} | {value["name"]:<20} | {value["price"]:<15} | {value["status"]:<10}')
                print('-'*len(header))
        case "2":
            print('-- TẠO MỚI ĐƠN HÀNG --')
            id_order = input('Nhập mã đơn hàng: ').strip().upper()
            for value in orders:
                if value["id"] == id_order:
                    print('[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống!!')
                    break
            else:
                name_agency = input('Nhập tên đại lý: ')
                price_order = input('Nhập giá trị đơn hàng: ')
                orders.append(
                    {
                        "id":id_order,
                        "name":name_agency,
                        "price":price_order,
                        "status":"Unpaid"
                    }
                )
                print(f'[Thành công]: Đơn hàng {id_order} đã được tạo thành công!!')

        case "3":
            print('-- CẬP NHẬP TRẠNG THÁI THANH TOÁN --')
            id_update = input('Nhập mã đơn hàng cần cập nhập: ').strip().upper()
            for value in orders:
                if value["id"] == id_update:
                    if value["status"] == "Unpaid":
                        value["status"] = "Paid"
                        print(f'Tìm thấy đơn hàng của: {value["name"]} (Gía trị: {value["price"]})')
                        print(f'Đơn hàng {id_update} đã được cập nhập trạng thái thanh toán!!')
                        break
                    else:
                        print('Đơn hàng đã được thanh toán trước đó!!')
                        break
            else:
                print(f'Không tìm thấy đơn hàng nào có mã {id_update}')

        case "4":
            total_revenue = 0
            discount = 0
            print('-- BÁO CÁO TÀI CHÍNH DOANH NGHIỆP --')
            for value in orders:
                if value["status"] == "Paid":
                    total_revenue += value["price"]
            print(f'Tổng thanh thu là: {total_revenue:,} VNĐ')

            if total_revenue >= 100000000:
                discount = int(total_revenue * 0.05)
                print('Tỷ lệ chiết khấu áp dụng là 5%')
                print(f'Số tiền chiết khấu đại lý nhận lại: {discount:,} VNĐ')
            else:
                print('Tỷ lệ chiết khấu áp dụng là 0%')
                print(f'Số tiền chiết khấu đại lý nhận lại: 0 VNĐ')

        case "5":
            print('Chương trình đã được thoát!!!')
            break
        case _:
            print('Lựa chọn không hợp lệ, Vui lòng nhập lại...')