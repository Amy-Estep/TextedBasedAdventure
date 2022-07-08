class SpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Spider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

