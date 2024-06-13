import random
from battle_moves import headbonk, spikebonk, dive, spin


class Enemy:
    def __init__(self, name, hp, attack, defense, moves_list, special=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves_list = moves_list
        self.special = special
        # Special will be spike, wings, or any other weird behaviors

    def __repr__(self):
        return f"{self.name}, {self.hp} hp, {self.attack} attack, {self.defense} defense."

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = random.choice(self.moves_list)
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


goomba = Enemy("Goomba", 2, 1, 0, [headbonk])
spiky_goomba = Enemy("Spiky Goomba", 2, 2, 0, [spikebonk], "spike")
paragoomba = Enemy("Paragoomba", 2, 1, 0, [dive], "wings")
spinia = Enemy("Spinia", 3, 1, 0, [spin])
