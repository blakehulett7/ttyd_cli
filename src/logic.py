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
        command = "None"
        while not command.isdigit() or int(command) not in [i for i in range(1, len(enemy_list) + 2)]:
            print("")
            print("-----Mario's Turn-----")
            for move in self.moves_list:
                i = self.moves_list.index(move) + 1
                print(f"{i}. {move.name}")
            print("")
            command = input("Choose an action: ")
        if int(command) == 1:
            print("Jump")
        if int(command) == 2:
            print("Hammer")

    def target_selection(self, enemy_list):
        confirmation = "None"
        while confirmation not in ["Y", "y"]:
            command = "None"
            while not command.isdigit() or int(command) - 1 not in [i for i in range(len(enemy_list) + 1)]:
                print("")
                print("-----Enemies-----")
                for enemy in enemy_list:
                    i = enemy_list.index(enemy) + 1
                    print(f"{i}. {enemy.name}")
                i += 1
                print(f"{i}. Go back")
                print("")
                command = input("Choose a target: ")
            if int(command) == i:
                return None
            index = int(command) - 1
            selection = enemy_list[index]
            confirmation = input(f"\nYou will target {
                selection.name}, is this ok?(Y/n): ")
        return selection

    def battle_jump(self, target):
        damage_calculation = self.jump.damage - target.defense
        input(f"\nMario jumps on {target.name} for {
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
