from random import choice
order_list = ["GE001", "GE002", "GE003"]
while  True:
    print("====== Hệ thống quản lí đơn hàng grap experss========\n"
          "1. Hiển thị danh sách đơn hàng\n"
          "2. Thêm đơn hàng mới\n"
          "3. Xóa đơn hàng theo mã\n"
          "4. Thoát chương trình\n")
    choice = input('Nhập vào lưa chọn của bạn (1-4): ')
    match choice:
        case "1":
            if not order_list:
                print('Danh sách rỗng!!')
            else:
                print("Danh sách đơn hàng hiện tại:")
                for index, value in enumerate(order_list):
                    print(f'{index+1}. {value}')

        case "2":
            id_new = input('Nhập vào mã đơn hàng mới: ').strip().upper()
            order_list.append(id_new)
            print('ĐÃ THÊM ĐƠN HÀNG MỚI!')

        case "3":
            delete_id_order = input('Nhập vào mã đơn hàng muốn xóa: ').strip().upper()

            if delete_id_order in order_list:
                order_list.remove(delete_id_order)
                print(f'Đã xóa đơn hàng có mã {delete_id_order}')
            else:
                print('Không tìm thấy mã đơn hàng cần xóa.')

        case "4":
            print('Thoát chương trình!!!')
            break

