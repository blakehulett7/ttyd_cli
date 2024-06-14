import random
from battle_moves import body_slam, headbonk, spikebonk, dive, spin


class Enemy:
    def __repr__(self):
        return f"{self.name}, {self.hp} hp, {self.attack} attack, {self.defense} defense."

    def turn(self, target):
        input(f"\n-----{self.name}'s turn-----")
        selected_move = random.choice(self.moves_list)
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Lord_Crump(Enemy):
    def __init__(self):
        self.name = "Lord Crump"
        self.hp = 5
        self.attack = 1
        self.defense = 0
        self.special = None

    def turn(self, formation):
        input(f"\n-----{self.name}'s turn-----")
        target = random.choice(formation)
        selected_move = body_slam
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Goomba(Enemy):
    def __init__(self):
        self.name = "Goomba"
        self.hp = 2
        self.attack = 1
        self.defense = 0
        self.special = None

    def turn(self, formation):
        input(f"\n-----{self.name}'s turn-----")
        target = random.choice(formation)
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

    def turn(self, formation):
        input(f"\n-----{self.name}'s turn-----")
        target = random.choice(formation)
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

    def turn(self, formation):
        input(f"\n-----{self.name}'s turn-----")
        target = random.choice(formation)
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

    def turn(self, formation):
        input(f"\n-----{self.name}'s turn-----")
        target = formation[0]
        selected_move = spin
        selected_move.battle(self, target)
        input(f"\nend of {self.name}'s turn")


class Blooper(Enemy):
    def __init__(self):
        self.name = "Blooper"
        self.hp = 12
        self.attack = 1
        self.defense = 0
        self.special = None
        self.left_tentacle = True
        self.right_tentacle = True
        self.stunned = False
        self.been_stunned = False

    def turn(self, formation):
        input("\n-----Blooper's Turn-----")
        if self.stunned:
            self.stun_counter += 1
            if self.stun_counter == 2:
                input("\nBlooper gets back up")
                print("")
                self.stunned = False
            else:
                input("\nBlooper is still stunned...")
        else:
            if self.left_tentacle or self.right_tentacle:
                target = random.choice(formation)
                damage_calculation = self.attack - target.defense
                if self.left_tentacle and self.right_tentacle:
                    tentacle_side = random.choice(["left", "right"])
                elif self.left_tentacle:
                    tentacle_side = "left"
                else:
                    tentacle_side = "right"
                input(f"\nBlooper raises his {tentacle_side} tentacle...")
                input(f"and smacks {target.name} for {
                    damage_calculation} damage")
                print("")
                target.hp -= damage_calculation
            else:
                if not self.been_stunned:
                    self.been_stunned = True
                    self.stunned = True
                    self.stun_counter = 1
                    input("\nBlooper is stunned and his turn is skipped...")
                    print("")
                else:
                    target_1 = formation[0]
                    if len(formation) == 2:
                        target_2 = formation[1]
                    dc_1 = self.attack - target_1.defense
                    dc_2 = self.attack - target_2.defense
                    input("\nBlooper floats up a few paces...")
                    input(f"and sprays {target_1.name} and {target_2.name} with ink for {
                        dc_1} and {dc_2} damage, respectively")
                    target_1.hp -= dc_1
                    target_2.hp -= dc_2


class Blooper_Left(Enemy):
    def __init__(self):
        self.name = "Left Tentacle"
        self.hp = 3
        self.attack = 1
        self.defense = 0
        self.special = "wings"

    def turn(self, formation):
        pass

    def death_event(self, allies):
        if len(allies) == 1:
            input("\nBlooper is stunned!")
        for ally in allies:
            ally.left_tentacle = False


class Blooper_Right(Enemy):
    def __init__(self):
        self.name = "Right Tentacle"
        self.hp = 3
        self.attack = 1
        self.defense = 0
        self.special = None

    def turn(self, formation):
        pass

    def death_event(self, allies):
        if len(allies) == 1:
            input("\nBlooper is stunned!")
        for ally in allies:
            ally.right_tentacle = False
