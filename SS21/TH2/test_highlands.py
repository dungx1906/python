import unittest

from ex02 import calculate_total, add_to_order, InvalidQuantityError


class TestHighlandsPOS(unittest.TestCase):

    def test_calculate_total(self):
        """Kiểm tra xem hàm tính tổng số tiền hoạt động chính xác không."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]

        result = calculate_total(mock_order)

        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Kiểm tra xem hàm add_to_order có ném lỗi InvalidQuantityError khi số lượng <= 0."""
        # Truyền vào mã hợp lệ "T1" nhưng số lượng âm "-1"
        # Hàm assertRaises sẽ kiểm tra xem ngoại lệ InvalidQuantityError có thực sự được kích hoạt không
        with self.assertRaises(InvalidQuantityError):
            add_to_order("T1", "-1")


if __name__ == '__main__':
    unittest.main()