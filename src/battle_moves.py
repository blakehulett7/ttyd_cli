class Move:
    def __init__(self, name, description, damage, aerial, walkup):
        self.name = name
        self.description = description
        self.damage = damage
        self.aerial = aerial
        self.walkup = walkup

    def __repr__(self):
        return f"({self.name}, damage is {self.damage}, aerial {self.aerial}, walkup {self.walkup})"


class Enemy_Move:
    def __init__(self, name, damage, latch):
        self.name = name
        self.damage = damage
        self.latch = latch


body_slam = Enemy_Move("Body Slam", 1, False)
