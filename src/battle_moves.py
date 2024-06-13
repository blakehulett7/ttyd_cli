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
    def __init__(self, name, damage, latch=False):
        self.name = name
        self.damage = damage
        self.latch = latch

    def battle(self, user, target):
        damage_calculation = self.damage - target.defense
        input(f"\n{user.name} {self.name}s {target.name} for {
              damage_calculation} damage.")
        target.hp -= damage_calculation

# Partner Moves


# Enemy Moves
body_slam = Enemy_Move("Body Slam", 1, False)
headbonk = Enemy_Move("Headbonk", 1)
spikebonk = Enemy_Move("Spikebonk", 2)
dive = Enemy_Move("Dive", 1)
spin = Enemy_Move("Spin", 1)
