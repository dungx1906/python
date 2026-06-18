class NetflixAccount:
    """
    Class quản lý tài khoản Netflix.
    """

    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        """
        Chỉ hiển thị mật khẩu đã được che.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Kiểm tra mật khẩu mới.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        """
        Read-only property.
        """
        return self.__plan

    @staticmethod
    def validate_email(email):
        """
        Kiểm tra email hợp lệ.
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Cập nhật giới hạn profile toàn hệ thống.
        """
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        """
        Thêm profile mới.
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    def upgrade_plan(self, new_plan):
        """
        Nâng cấp gói cước.
        """
        valid_plans = ["Basic", "Standard", "Premium"]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan
        print(f"Đã nâng cấp lên gói {new_plan}")

    def display_info(self):
        """
        Hiển thị thông tin tài khoản.
        """
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.plan}")
        print(f"Danh sách Profile: {self.profiles}")
        print(
            f"Số lượng Profile: {len(self.profiles)}/{NetflixAccount.max_profiles}"
        )


current_account = None

while True:
    print("""
===== NETFLIX ACCOUNT MANAGER =====
1. Đăng ký tài khoản mới
2. Xem thông tin tài khoản
3. Thêm người xem
4. Nâng cấp gói cước
5. Cập nhật chính sách Netflix
6. Thoát chương trình
==================================
""")

    choice = input("Chọn chức năng (1-6): ")

    # Đăng ký
    while True:
        print("""
    ===== NETFLIX ACCOUNT MANAGER =====
    1. Đăng ký tài khoản mới
    2. Xem thông tin tài khoản
    3. Thêm người xem
    4. Nâng cấp gói cước
    5. Cập nhật chính sách Netflix
    6. Thoát chương trình
    ==================================
    """)

        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case "1":
                print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")

                while True:
                    email = input("Nhập Email: ")

                    if NetflixAccount.validate_email(email):
                        break

                    print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")

                account = NetflixAccount(email)

                while True:
                    try:
                        password = input("Nhập mật khẩu: ")
                        account.password = password
                        break

                    except ValueError as e:
                        print(e)

                current_account = account
                print("Đăng ký tài khoản thành công!")

            case "2":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    current_account.display_info()

            case "3":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                    continue

                print("\n--- THÊM PROFILE ---")
                profile_name = input("Nhập tên Profile: ")
                current_account.add_profile(profile_name)

            case "4":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                    continue

                print("\n--- NÂNG CẤP GÓI CƯỚC ---")
                print("1. Basic")
                print("2. Standard")
                print("3. Premium")

                option = input("Chọn gói: ")

                match option:
                    case "1":
                        current_account.upgrade_plan("Basic")
                    case "2":
                        current_account.upgrade_plan("Standard")
                    case "3":
                        current_account.upgrade_plan("Premium")
                    case _:
                        print("Lựa chọn không hợp lệ")

            case "5":
                print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")

                try:
                    new_limit = int(input("Nhập giới hạn Profile mới: "))

                    if new_limit <= 0:
                        print("Giới hạn phải lớn hơn 0")
                    else:
                        NetflixAccount.update_max_profiles(new_limit)
                        print(
                            f"Đã cập nhật giới hạn Profile toàn hệ thống thành {NetflixAccount.max_profiles}"
                        )

                except ValueError:
                    print("Vui lòng nhập số hợp lệ")

            case "6":
                print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
                break

            case _:
                print("Lựa chọn không hợp lệ")