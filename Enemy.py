class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=30, damage=15)

class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=10, damage=2)
