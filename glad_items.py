class Item():
    def __init__(self, name, value, tradable, limit, amount, heal, attack_buff, defense_buff, speed_buff):
        self.name = name
        self.value = value
        self.tradable = tradable
        self.limit = limit
        self.amount = amount
        self.heal = heal
        self.attack_buff = attack_buff
        self.defense_buff = defense_buff
        self.speed_buff = speed_buff

#:Non-weapon items
class Gold(Item):
    def __init__(self, amount):
        super().__init__("gold", 1, True, 100, amount, None, None, None, None)

class Potion(Item):
    def __init__(self, amount):
        super().__init__("potions", 10, True, 5, amount, 5, None, None, None)
        self.heal_amount = 5

class Sweetcakes(Item):
    def __init__(self, amount):
        super().__init__("sweetcakes", 5, True, 5, amount, 2, None, None, None)
        self.heal_amount = 2

#: Weapons
class Weapon(Item):
    def __init__(self, name, value, w_type, speed, damage):
        super().__init__(name, value, True, 1, 1, None, None, None, None)
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


#: Armor items
class Armor(Item):
    def __init__(self, name, value, defense, weight):
        super().__init__(name, value, True, 1, 1, None, None, None, None)
        self.defense = defense
        self.weight = weight

class Chainmail(Armor):
    def __init__(self):
        super().__init__("Chainmail", 3, 4, 3)

class Platemail(Armor):
    def __init__(self):
        super().__init__("Platemail", 5, 8, 6)

class Tunic(Armor):
    def __init__(self):
        super().__init__("Tunic", 0, 0, 0)
