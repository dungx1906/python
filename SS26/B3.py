from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage()

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        if isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]


def find_champion(champion_id):
    return next(
        (c for c in champion_pool if c.champion_id.upper() == champion_id.upper()),
        None
    )


while True:
    print("""
===== RIKKEI RPG AUTO-BATTLER =====
1. Hiển thị bể tướng
2. Thêm quân cờ mới
3. So sánh 2 quân cờ
4. Tính tổng chiến lực đội hình
5. Thoát
==================================
""")

    match input("Chọn chức năng (1-5): "):

        case "1":
            print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
            print(f"{'Mã':<8} | {'Tên tướng':<20} | {'Hệ':<8} | {'HP':<6} | {'ATK':<6} | {'Chỉ số riêng':<20} | {'Chiến lực'}")
            print("-" * 110)

            for c in champion_pool:
                champion_type = "Warrior" if isinstance(c, Warrior) else "Mage"
                special = f"Armor: {c.shield_bonus}" if isinstance(c, Warrior) else f"Mana: {c.ability_power}"

                print(
                    f"{c.champion_id:<8} | {c.name:<20} | {champion_type:<8} | "
                    f"{c.base_hp:<6} | {c.base_atk:<6} | {special:<20} | "
                    f"{c.get_combat_power():.0f}"
                )

            print("-" * 110)

        case "2":
            print("\n1. Warrior\n2. Mage")

            champion_type = input("Chọn hệ tướng: ")
            champion_id = input("Nhập mã tướng: ").upper()

            if find_champion(champion_id):
                print("Mã tướng đã tồn tại!")
                continue

            name = input("Nhập tên tướng: ")

            try:
                hp = int(input("Nhập HP: "))
                atk = int(input("Nhập ATK: "))

                if champion_type == "1":
                    champion = Warrior(
                        champion_id,
                        name,
                        hp,
                        atk,
                        int(input("Nhập Armor: "))
                    )
                elif champion_type == "2":
                    champion = Mage(
                        champion_id,
                        name,
                        hp,
                        atk,
                        float(input("Nhập Ability Power: "))
                    )
                else:
                    print("Lựa chọn không hợp lệ!")
                    continue

                champion_pool.append(champion)

                print(
                    f"Thêm tướng thành công!"
                    f"\nMã: {champion.champion_id}"
                    f" | Tên: {champion.name}"
                    f" | Chiến lực: {champion.get_combat_power():.0f}"
                )

            except ValueError:
                print("Dữ liệu không hợp lệ!")

        case "3":
            print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")

            champion1 = find_champion(input("Nhập mã tướng thứ nhất: ").upper())
            champion2 = find_champion(input("Nhập mã tướng thứ hai: ").upper())

            if not champion1:
                print("Mã tướng thứ nhất không hợp lệ!")
                continue

            if not champion2:
                print("Mã tướng thứ hai không hợp lệ!")
                continue

            print(
                f"\n{champion1.champion_id} - {champion1.name}"
                f" | Chiến lực: {champion1.get_combat_power():.0f}"
            )

            print(
                f"{champion2.champion_id} - {champion2.name}"
                f" | Chiến lực: {champion2.get_combat_power():.0f}"
            )

            stronger = champion1 if champion1 > champion2 else champion2
            weaker = champion2 if champion1 > champion2 else champion1

            print(
                f"Kết quả: {stronger.champion_id} - {stronger.name}"
                f" mạnh hơn {weaker.champion_id} - {weaker.name}"
            )

        case "4":
            print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---")

            team = []

            for champion_id in input(
                "Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: "
            ).split(","):

                champion = find_champion(champion_id.strip())

                if champion:
                    team.append(champion)
                else:
                    print(f"Mã tướng {champion_id.strip()} không hợp lệ, bỏ qua!")

            if not team:
                print("Không có tướng hợp lệ.")
                continue

            print("\nDanh sách đội hình:")

            for i, champion in enumerate(team, 1):
                print(
                    f"{i}. {champion.champion_id} - {champion.name}"
                    f" | Chiến lực: {champion.get_combat_power():.0f}"
                )

            print(f"Tổng chiến lực đội hình: {sum(team):.0f}")

        case "5":
            print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")