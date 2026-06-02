#Phân tích lỗi:
'''
Phần tử "GE100-FAST" được chèn vào vị trí đầu tiên (index 0). Các phần tử cũ bị đẩy lùi xuống sau 1 vị trí.
Vì sau khi chèn "GE100-FAST" vào vị trí 0, toàn bộ index của các phần tử phía sau tăng lên 1 đơn vị. Lúc này "GE101" chuyển sang index 1, còn "GE102-WRONG" chuyển sang index 2.
Đơn hàng "GE102-WRONG" đang nằm ở index 2.
danh sách hiện tại đang là ["GE100-FAST", "GE101", "GE102-UPDATED", "GE103-CANCEL", "GE104"]. Phần tử ở index 3 chính là "GE103-CANCEL". Do đó, dòng lệnh express_orders.pop(3) thực chất đã xóa đúng đơn hàng bị hủy "GE103-CANCEL".
express_orders.remove("GE103-CANCEL").
Sẽ lấy và xóa phần tử ở cuối cùng của danh sách.
Yêu cầu bài toán là "Lấy đơn hàng đầu tiên ra để bắt đầu giao". Nếu gọi .pop() không truyền tham số, Python sẽ lấy phần tử cuối cùng ("GE104"), dẫn đến việc lấy sai đơn hàng cần giao.
Cần truyền chỉ số 0 vào phương thức pop: current_order = express_orders.pop(0).
cần sửa:
-mã đơn hàng bị nhập sai

- Lấy đơn hàng đầu tiên ra để bắt đầu giao
'''

# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.pop(3)

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)