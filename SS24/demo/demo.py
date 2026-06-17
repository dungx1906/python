class Animal:
    def __init__(self, name, legs, sound):
        self.name = name
        self.legs = legs
        self.sound = sound


dog = Animal("chó", "4", "gau gau")
cat = Animal("mèo", "4", "meo meo")
snack = Animal("rắn", "0", "khè khè")

print(dog.name)
print(cat.name)
print(snack.name)

print(dog.legs)
print(cat.legs)
print(snack.legs)
