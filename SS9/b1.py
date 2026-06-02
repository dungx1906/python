'''
Sau khi chạy dòng lệnh delivery_orders.insert(0, "GE000"), danh sách thay đổi như thế nào?
-Phần tử "GE000" được chèn vào đầu danh sách (vị trí chỉ mục 0). Các phần tử phía sau tự động lùi xuống 1 vị trí.
-Danh sách lúc này trở thành: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"].
'''
'''
Vì sao dòng lệnh delivery_orders[1] = "GE002-UPDATED" sửa sai đơn hàng cần cập nhật?
-Vì sau khi đã chèn thêm "GE000" vào đầu, vị trí chỉ mục (index) của các phần tử cũ đã thay đổi. Đơn hàng "GE002" ban đầu ở vị trí 1 nay đã bị đẩy xuống vị trí số 2.
-Do đó, viết delivery_orders[1] sẽ vô tình sửa nhầm đơn hàng "GE001" thành "GE002-UPDATED".
'''
'''
Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index nào?
-Đơn hàng "GE002" đang nằm ở index 2.
'''
'''
Vì sao dòng lệnh delivery_orders.remove(3) gây lỗi?
-Vì phương thức .remove() trong Python tìm kiếm và xóa theo giá trị (value) chứ không phải theo vị trí (index). Chương trình báo lỗi ValueError: list.remove(x): x not in list do trong danh sách không có phần tử nào mang giá trị là số 3.
'''

# Phương thức remove() xóa phần tử theo giá trị
# Cần truyền chính xác giá trị chuỗi vào: delivery_orders.remove("GE003-CANCEL")
# Phương thức pop() dùng để xóa và trả về phần tử tại một vị trí xác định (nếu không truyền index, mặc định nó sẽ lấy và xóa phần tử cuối cùng của danh sách).
# Vì lệnh delivery_orders.pop() đã thực hiện lấy phần tử ra nhưng giá trị đó chưa được gán vào bất kỳ biến nào, dẫn đến việc biến transferred_order chưa hề tồn tại (gây lỗi NameError).
# Cần gán kết quả trả về của hàm .pop() vào biến: transferred_order = delivery_orders.pop().

# 1. Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# 2. Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# 3. Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")
# Lúc này danh sách là: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]

# 4. Sửa mã đơn hàng GE002 thành GE002-UPDATED (Sửa index từ 1 thành 2)
delivery_orders[2] = "GE002-UPDATED"

# 5. Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

# 6. Lấy đơn hàng cuối cùng ra và gán vào biến transferred_order
transferred_order = delivery_orders.pop()

# 7. In kết quả
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)