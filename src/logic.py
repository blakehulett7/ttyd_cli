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
        go_back = True
        while go_back:
            go_back = False
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
                print("\nYou've selected jump!")
                target = self.target_selection(enemy_list)
                if target == "Go Back":
                    go_back = True
                else:
                    self.battle_jump(target)
            if int(command) == 2:
                confirmed = False
                while not confirmed:
                    print("\nYou've selected hammer!")
                    answer = input(f"You will target {
                        enemy_list[0].name}, is this ok? (Y/n): ")
                    if answer in ["N", "n"]:
                        go_back = True
                        confirmed = True
                    if answer in ["Y", "y"]:
                        confirmed = True
                self.battle_hammer(enemy_list[0])

    def target_selection(self, enemy_list):
        confirmed = False
        while not confirmed:
            valid_selection = False
            while not valid_selection:
                print("\n-----Enemies-----")
                for enemy in enemy_list:
                    j = enemy_list.index(enemy) + 1
                    print(f"{j}. {enemy.name}")
                j += 1
                print(f"{j}. Go Back")
                print("")
                selection = input("Choose a target: ")
                if selection.isdigit() and int(selection) in [i for i in range(1, len(enemy_list) + 2)]:
                    valid_selection = True
            if int(selection) == j:
                confirmed = True
                result = "Go Back"
            else:
                valid_answer = False
                while not valid_answer:
                    target_index = int(selection) - 1
                    target = enemy_list[target_index]
                    answer = input(f"You will target {
                        target.name}, is this ok? (Y/n): ")
                    if answer in ["Y", "y", "N", "n"]:
                        valid_answer = True
                if answer in ["Y", "y"]:
                    result = target
                    confirmed = True
        return result

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
