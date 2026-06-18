from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return False

        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return self

        return Weapon(
            f"Fusion({self.name} + {other.name})",
            self.base_damage + other.base_damage,
            self.upgrade_level + other.upgrade_level
        )


class MagicMixin:
    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} đang phát sáng ma thuật!")


class MagicSword(Weapon, MagicMixin):
    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


inventory = []


def input_positive(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số nguyên!")


while True:
    print("""
===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS ===================
1. Xem kho vũ khí & Sát thương tổng
2. Rèn Vũ khí Vật lý
3. Rèn Kiếm Ma Thuật
4. Thẩm định vũ khí
5. Dung hợp vũ khí
6. Thoát game
======================================================
""")

    choice = input("Chọn chức năng (1-6): ")

    match choice:

        case "1":
            print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")

            if not inventory:
                print("Kho vũ khí hiện đang trống.")
                print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
                continue

            print(
                f"{'STT':<5} | {'Tên vũ khí':<30} | "
                f"{'Loại':<12} | {'Cấp':<5} | {'Sát thương'}"
            )
            print("-" * 80)

            for i, item in enumerate(inventory, 1):
                print(
                    f"{i:<5} | "
                    f"{item.name:<30} | "
                    f"{type(item).__name__:<12} | "
                    f"{item.upgrade_level:<5} | "
                    f"{item.calculate_total_damage()}"
                )

        case "2":
            print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

            name = input("Nhập tên vũ khí: ")
            damage = input_positive("Nhập sát thương gốc: ")
            level = input_positive("Nhập cấp cường hóa: ")

            weapon = Weapon(name, damage, level)
            inventory.append(weapon)

            print("\n>> Rèn vũ khí vật lý thành công!")
            print(f"Tên vũ khí: {weapon.name}")
            print("Loại: Weapon")
            print(f"Cấp cường hóa: {weapon.upgrade_level}")
            print(f"Sát thương tổng: {weapon.calculate_total_damage()}")

        case "3":
            print("\n--- RÈN KIẾM MA THUẬT ---")

            name = input("Nhập tên kiếm ma thuật: ")
            damage = input_positive("Nhập sát thương gốc: ")
            level = input_positive("Nhập cấp cường hóa: ")
            magic_power = input_positive("Nhập sức mạnh phép thuật: ")

            sword = MagicSword(
                name,
                damage,
                level,
                magic_power
            )

            inventory.append(sword)

            print("\n>> Rèn kiếm ma thuật thành công!")
            print(f"Tên vũ khí: {sword.name}")
            print("Loại: MagicSword")
            print(f"Cấp cường hóa: {sword.upgrade_level}")
            print(f"Sát thương gốc: {sword.base_damage}")
            print(f"Sức mạnh phép thuật: {sword.magic_power}")
            print(f"Sát thương tổng: {sword.calculate_total_damage()}")

        case "4":
            print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

            if len(inventory) < 2:
                print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
                continue

            w1, w2 = inventory[0], inventory[1]

            print(
                f"Vũ khí thứ nhất:\n"
                f"{w1.name} | Loại: {type(w1).__name__} | "
                f"Sát thương: {w1.calculate_total_damage()}"
            )

            print(
                f"\nVũ khí thứ hai:\n"
                f"{w2.name} | Loại: {type(w2).__name__} | "
                f"Sát thương: {w2.calculate_total_damage()}"
            )

            if w1 > w2:
                print(f"\nKết quả: {w1.name} mạnh hơn {w2.name}.")
            elif w2 > w1:
                print(f"\nKết quả: {w2.name} mạnh hơn {w1.name}.")
            else:
                print("\nKết quả: Hai vũ khí có sức mạnh ngang nhau.")

        case "5":
            print("\n--- DUNG HỢP VŨ KHÍ ---")

            if len(inventory) < 2:
                print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
                continue

            w1, w2 = inventory[0], inventory[1]

            print("Đang dung hợp 2 vũ khí đầu tiên trong kho...\n")

            print(
                f"Vũ khí 1: {w1.name} | "
                f"Cấp: {w1.upgrade_level} | "
                f"Sát thương: {w1.calculate_total_damage()}"
            )

            print(
                f"Vũ khí 2: {w2.name} | "
                f"Cấp: {w2.upgrade_level} | "
                f"Sát thương gốc: {w2.base_damage}"
            )

            new_weapon = w1 + w2

            inventory.pop(0)
            inventory.pop(0)

            inventory.append(new_weapon)

            print("\n>> Dung hợp vũ khí thành công!")
            print(f"Đã xóa khỏi kho: {w1.name}")
            print(f"Đã xóa khỏi kho: {w2.name}")

            print(f"\nVũ khí mới: {new_weapon.name}")
            print("Loại: Weapon")
            print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
            print(
                f"Sát thương tổng: "
                f"{new_weapon.calculate_total_damage()}"
            )

        case "6":
            print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")