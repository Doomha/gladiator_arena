class Item():
    def __init__(self, name, value, tradable, limit, amount):
        self.name = name
        self.value = value
        self.tradable = tradable
        self.limit = limit
        self.amount = amount

#:Non-weapon items
class Gold(Item):
    def __init__(self, amount):
        super().__init__("gold", 1, True, 100, amount)

class Potion(Item):
    def __init__(self, amount):
        super().__init__("potions", 5, True, 5, amount)

class Ale(Item):
    def __init__(self, amount):
        super().__init__("ale", 10, True, 5, amount)

#: Weapons
class Weapon(Item):
    def __init__(self, name, value, w_type, speed, damage):
        super().__init__(name, value, True, 1, 1)
        self.w_type = w_type
        self.speed = speed
        self.damage = damage

#: Ranged weapons
class Ranged_weapon(Weapon):
    def __init__(self, name, value, speed, damage):
        super().__init__(name, value, "ranged", speed, damage)

class Bow(Ranged_weapon):
    def __init__(self):
        super().__init__("Bow", 6, 5, 7)

#: Melee weapons
class Melee_weapon(Weapon):
    def __init__(self, name, value, speed, damage):
        super().__init__(name, value, "melee", speed, damage)

class Sword(Melee_weapon):
    def __init__(self):
        super().__init__("Sword", 6, 6, 6)

class Spear(Melee_weapon):
    def __init__(self):
        super().__init__("Spear", 6, 4, 8)

class Rock(Melee_weapon):
    def __init__(self):
        super().__init__("Rock", 1, 1, 1)


class Magic_weapon(Weapon):
    def __init__(self, name, value, speed, damage):
        super().__init__(name, value, "magic", speed, damage)

#: Armor items
class Armor(Item):
    def __init__(self, name, value, defense, weight):
        super().__init__(name, value, True, 1, 1)
        self.defense = defense
        self.weight = weight

class Chainmail(Armor):
    def __init__(self):
        super().__init__("Chainmail", 3, 2, 3)

class Platemail(Armor):
    def __init__(self):
        super().__init__("Platemail", 4, 6, 6)

class Tunic(Armor):
    def __init__(self):
        super().__init__("Tunic", 0, 0, 0)
