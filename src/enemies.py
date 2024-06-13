import random
from battle_moves import headbonk, spikebonk, dive


class Enemy:
    def __init__(self, name, hp, defense, moves_list, special=None):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.moves_list = moves_list
        self.special = special
        # Special will be spike, wings, or any other weird behaviors

    def __repr__(self):
        return f"({self.name}, {self.hp} hp, {self.defense} defense.)"

    def turn(self, target):
        print(f"-----{self.name}'s turn-----")
        input()
        selected_move = random.choice(self.moves_list)
        selected_move.battle(self, target)
        input()
        print(f"end of {self.name}'s turn")


goomba = Enemy("Goomba", 2, 0, [headbonk])
spiky_goomba = Enemy("Spiky Goomba", 2, 0, [spikebonk], "spike")
paragoomba = Enemy("Paragoomba", 2, 0, [dive], "wings")
