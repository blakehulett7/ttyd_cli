import random
from battle_moves import headbonk, spikebonk, dive, spin


class Enemy:
    def __repr__(self):
        return f"{self.name}, {self.hp} hp, {self.attack} attack, {self.defense} defense."

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = random.choice(self.moves_list)
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Goomba(Enemy):
    def __init__(self):
        self.name = "Goomba"
        self.hp = 2
        self.attack = 1
        self.defense = 0
        self.special = None

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = headbonk
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Spiky_Goomba(Enemy):
    def __init__(self):
        self.name = "Spiky Goomba"
        self.hp = 2
        self.attack = 2
        self.defense = 0
        self.special = "spike"

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = spikebonk
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Paragoomba(Enemy):
    def __init__(self):
        self.name = "Paragoomba"
        self.hp = 2
        self.attack = 1
        self.defense = 0
        self.special = "wings"

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = dive
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Spinia(Enemy):
    def __init__(self):
        self.name = "Spinia"
        self.hp = 3
        self.attack = 1
        self.defense = 0
        self.special = None

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = spin
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")
