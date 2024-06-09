from battle_moves import Move


class Game_Master:
    def __init__(self):
        self.room = "Rogueport Docks"


class Mario:
    def __init__(self):
        self.hp = 10
        self.fp = 5
        self.bp = 3
        self.defense = 0
        self.jump = Move("Jump", "Jump on an enemy", 1, True, False)
        self.hammer = Move(
            "Hammer", "Whack an enemy with your hammer", 2, False, True)
        self.moves_list = [self.jump, self.hammer]

    def __repr__(self):
        return f"(Mario! {self.hp} hp, {self.fp} fp, {self.bp} bp)"

    def turn(self, enemy_list):
        print("")
        print("-----Mario's Turn-----")
        for move in self.moves_list:
            i = self.moves_list.index(move) + 1
            print(f"{i}. {move.name}")
        print("")
        command = input("Choose an action: ")
        if (not command.isdigit()
            or int(command) - 1 < 0
                or int(command) - 1 >= len(self.moves_list)):
            print("\nInvalid command, try again.")
            self.turn(enemy_list)
        else:
            move_index = int(command)
        if move_index == 1:
            print("\nYou've selected jump")
            input()
            self.target_selection(enemy_list)
            self.battle_jump(enemy_list[0])
        elif move_index == 2:
            print("\nYou've selected hammer!")
            confirmation = 0
            while confirmation not in ["Y", "y", "N", "n"]:
                confirmation = input(f"You will target {
                    enemy_list[0].name}, is this ok?(Y/n): ")
            if confirmation in ["N", "n"]:
                self.turn(enemy_list)
            elif confirmation in ["Y", "y"]:
                self.battle_hammer(enemy_list[0])

    def target_selection(self, enemy_list):
        print("Select a target:")
        for enemy in enemy_list:
            print(enemy.name)
        command = 0

    def battle_jump(self, target):
        damage_calculation = self.jump.damage - target.defense
        input(f"Mario jumps on {target.name} for {
              damage_calculation} damage")
        print(f"Mario jumps on {target.name} for {damage_calculation} damage")
        target.hp -= damage_calculation * 2

    def battle_hammer(self, target):
        damage_calculation = self.hammer.damage - target.defense
        print(f"\nMario whacks {target.name} with a hammer for {
              damage_calculation} damage.")
        target.hp -= damage_calculation


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
