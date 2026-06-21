from abc import ABC, abstractmethod


class BaseProduct(ABC):
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, product_name, stock_quantity=0):
        self.product_code = product_code
        self.product_name = product_name
        self._BaseProduct__stock_quantity = stock_quantity

    @property
    def stock_quantity(self):
        return self._BaseProduct__stock_quantity

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = " ".join(value.strip().upper().split())

    @abstractmethod
    def import_stock(self, quantity):
        pass

    @abstractmethod
    def export_stock(self, quantity):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    def __lt__(self, other):
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity

    @staticmethod
    def validate_product_code(product_code):
        return (
            len(product_code) == 10
            and product_code[0].isalpha()
        )

    @classmethod
    def update_warehouse_name(cls, new_name):
        cls.warehouse_name = new_name

    def _increase_stock(self, quantity):
        self._BaseProduct__stock_quantity += quantity

    def _decrease_stock(self, quantity):
        self._BaseProduct__stock_quantity -= quantity


class ColdStorageProduct(BaseProduct):
    def __init__(
        self,
        product_code,
        product_name,
        required_temperature,
        stock_quantity=0
    ):
        super().__init__(
            product_code,
            product_name,
            stock_quantity
        )
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        self._increase_stock(quantity)

        print(f"Nhập kho thành công: {quantity} đơn vị")
        print(f"Tồn kho hiện tại: {self.stock_quantity}")

    def export_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        loss = quantity * 0.05
        total = quantity + loss

        if total > self.stock_quantity:
            print("Không đủ tồn kho.")
            return

        self._decrease_stock(total)

        print("Xuất kho thành công!")
        print(f"Số lượng yêu cầu: {quantity}")
        print(f"Hao hụt bảo quản: {loss}")
        print(f"Tổng khấu trừ: {total}")
        print(f"Tồn kho còn lại: {self.stock_quantity}")

    def apply_cooling_cost(self):
        cost = self.stock_quantity * 3000

        print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")
        print(f"Tồn kho: {self.stock_quantity}")
        print(f"Nhiệt độ yêu cầu: {self.required_temperature}°C")
        print(f"Chi phí phát sinh: +{cost:,.0f} VND")


class HazardousProduct(BaseProduct):
    def __init__(
        self,
        product_code,
        product_name,
        max_safety_limit,
        stock_quantity=0
    ):
        super().__init__(
            product_code,
            product_name,
            stock_quantity
        )
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        if self.stock_quantity + quantity > self.max_safety_limit:
            raise ValueError(
                f"Vượt quá hạn mức an toàn "
                f"({self.max_safety_limit})"
            )

        self._increase_stock(quantity)

        print("Nhập kho thành công!")
        print(f"Tồn kho hiện tại: {self.stock_quantity}")

    def export_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        if quantity > self.stock_quantity:
            print("Không đủ tồn kho.")
            return

        self._decrease_stock(quantity)

        print("Xuất kho thành công!")
        print(f"Tồn kho còn lại: {self.stock_quantity}")

class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    def __init__(self, product_code, product_name, required_temperature, max_safety_limit, stock_quantity=0):
        BaseProduct.__init__(self, product_code, product_name, stock_quantity)
        self.required_temperature = required_temperature
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        if self.stock_quantity + quantity > self.max_safety_limit:
            raise ValueError(f"Giao dịch thất bại! Vượt quá hạn mức an toàn ({self.max_safety_limit}).")

        self._increase_stock(quantity)
        print("Nhập kho Hybrid thành công!")
        print(f"Tồn kho hiện tại: {self.stock_quantity}")

    def export_stock(self, quantity):
        if quantity <= 0:
            print("Số lượng không hợp lệ.")
            return

        loss = quantity * 0.05
        total = quantity + loss

        if total > self.stock_quantity:
            print("Không đủ tồn kho.")
            return

        self._decrease_stock(total)

        print("Xuất kho Hybrid thành công!")
        print(f"Số lượng yêu cầu: {quantity}")
        print(f"Hao hụt: {loss}")
        print(f"Tổng khấu trừ: {total}")
        print(f"Tồn kho còn lại: {self.stock_quantity}")

class FedExCarrier:
    def ship_package(self, product, quantity):
        print(f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        product.export_stock(quantity)


class DHLCarrier:
    def ship_package(self, product, quantity):
        print(f"[Hệ thống DHL]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        product.export_stock(quantity)

def dispatch_to_carrier(carrier_agent, product, quantity):
    try:
        carrier_agent.ship_package(product, quantity)

        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Đơn vị vận chuyển đã tiếp nhận {quantity} đơn vị.")
        print(f"Tồn kho cập nhật: {product.stock_quantity}")

    except AttributeError:
        print("Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật")

    except Exception as e:
        print("Lỗi:", e)

def display_product(product):
    print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
    print("Loại sản phẩm:", type(product).__name__)
    print("Chuỗi kho:", product.warehouse_name)
    print("Mã sản phẩm:", product.product_code)
    print("Tên sản phẩm:", product.product_name)
    print(f"Tồn kho: {product.stock_quantity}")

    if isinstance(product, (ColdStorageProduct, HybridPremiumProduct)):
        print(f"Nhiệt độ yêu cầu: {product.required_temperature}°C")

    if isinstance(product, (HazardousProduct, HybridPremiumProduct)):
        print(f"Hạn mức an toàn: {product.max_safety_limit}")

    print("\n--- MRO ---")
    for cls in product.__class__.mro():
        print(cls.__name__)

def select_product(products):
    if not products:
        print("Chưa có sản phẩm.")
        return None

    print("\n--- DANH SÁCH SẢN PHẨM ---")

    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.product_code} - {product.product_name} ({product.stock_quantity})")

    try:
        return products[int(input("Chọn sản phẩm: ")) - 1]
    except:
        print("Lựa chọn không hợp lệ.")
        return None

products = []
current_product = None

while True:
    print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
    print("1. Đăng ký mã hàng hóa mới")
    print("2. Xem thông tin & Kiểm tra MRO")
    print("3. Giao dịch Nhập / Xuất kho")
    print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
    print("5. Gộp lô hàng & So sánh tồn kho")
    print("6. Điều phối vận chuyển qua Đối tác thứ ba")
    print("7. Thoát chương trình")

    choice = input("Chọn chức năng (1-7): ")

    match choice:

        case "1":
            print("\n--- CHỌN LOẠI SẢN PHẨM ---")
            print("1. Cold Storage Product")
            print("2. Hazardous Product")
            print("3. Hybrid Premium Product")

            product_type = input("Chọn loại sản phẩm (1-3): ")
            product_code = input("Nhập mã sản phẩm 10 ký tự: ")

            if not BaseProduct.validate_product_code(product_code):
                print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng chữ.")
                continue

            product_name = input("Nhập tên sản phẩm: ")

            try:
                match product_type:

                    case "1":
                        temperature = float(input("Nhập nhiệt độ bảo quản: "))
                        current_product = ColdStorageProduct(
                            product_code,
                            product_name,
                            temperature,
                            100
                        )

                    case "2":
                        limit = int(input("Nhập hạn mức an toàn: "))
                        current_product = HazardousProduct(
                            product_code,
                            product_name,
                            limit,
                            100
                        )

                    case "3":
                        temperature = float(input("Nhập nhiệt độ bảo quản: "))
                        limit = int(input("Nhập hạn mức an toàn: "))

                        current_product = HybridPremiumProduct(
                            product_code,
                            product_name,
                            temperature,
                            limit,
                            100
                        )

                    case _:
                        print("Loại sản phẩm không hợp lệ.")
                        continue

                products.append(current_product)

                print("Đăng ký sản phẩm thành công!")
                print("Tên sản phẩm:", current_product.product_name)

            except Exception as e:
                print("Lỗi:", e)

        case "2":
            if not current_product:
                print("Hệ thống chưa có sản phẩm.")
                continue

            display_product(current_product)

        case "3":
            if not current_product:
                print("Hệ thống chưa có sản phẩm.")
                continue

            print("\n1. Nhập kho")
            print("2. Xuất kho")

            action = input("Chọn giao dịch (1-2): ")

            try:
                quantity = float(input("Nhập số lượng: "))

                match action:
                    case "1":
                        current_product.import_stock(quantity)

                    case "2":
                        current_product.export_stock(quantity)

                    case _:
                        print("Lựa chọn không hợp lệ.")

            except Exception as e:
                print("Lỗi:", e)

        case "4":
            if not current_product:
                print("Hệ thống chưa có sản phẩm.")
                continue

            if isinstance(current_product, (ColdStorageProduct, HybridPremiumProduct)):
                current_product.apply_cooling_cost()
            else:
                print("Sản phẩm này không hỗ trợ tính phí làm lạnh.")

        case "5":
            if len(products) < 2:
                print("Cần ít nhất 2 sản phẩm.")
                continue

            print(f"\nSản phẩm A: {current_product.product_name} ({current_product.stock_quantity})")

            other_product = select_product(products)

            if not other_product or other_product == current_product:
                print("Sản phẩm đối ứng không hợp lệ.")
                continue

            try:
                if current_product < other_product:
                    print("[Kết quả So sánh (__lt__)]: Tồn kho A ÍT HƠN tồn kho B.")
                else:
                    print("[Kết quả So sánh (__lt__)]: Tồn kho A KHÔNG ÍT HƠN tồn kho B.")

                total_stock = current_product + other_product

                print(f"[Kết quả Tổng hợp (__add__)]: {total_stock} đơn vị")

            except TypeError:
                print("Không thể so sánh dữ liệu.")

        case "6":
            if not current_product:
                print("Hệ thống chưa có sản phẩm.")
                continue

            print("\n1. FedEx")
            print("2. DHL")

            carrier_choice = input("Chọn đơn vị vận chuyển (1-2): ")

            try:
                quantity = float(input("Nhập số lượng bàn giao: "))

                match carrier_choice:
                    case "1":
                        carrier = FedExCarrier()

                    case "2":
                        carrier = DHLCarrier()

                    case _:
                        print("Đơn vị vận chuyển không hợp lệ.")
                        continue

                dispatch_to_carrier(carrier, current_product, quantity)

            except Exception as e:
                print("Lỗi:", e)

        case "7":
            print("\nCảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
            break

        case _:
            print("Vui lòng chọn từ 1 đến 7.")