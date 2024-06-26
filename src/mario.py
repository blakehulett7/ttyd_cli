from battle_moves import Move
from graphics import Colors


class Mario:
    def __init__(self):
        self.name = "Mario"
        self.star_points = 0
        self.paper_mode = []
        self.hp = 10
        self.fp = 5
        self.bp = 3
        self.defense = 0
        self.jump = Move("Jump", "Jump on an enemy", 1, True, False)
        self.hammer = Move(
            "Hammer", "Whack an enemy with your hammer", 2, False, True)
        self.moves_list = [self.jump, self.hammer]
        self.special_moves = []

    def __repr__(self):
        return f"Mario, {self.hp} hp, {self.fp} fp, {self.bp} bp"

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
                    target = self.auto_target(enemy_list)
                    if target:
                        answer = input(f"You will target {
                            target.name}, is this ok? (Y/n): ")
                        if answer in ["N", "n"]:
                            go_back = True
                            confirmed = True
                        if answer in ["Y", "y"]:
                            confirmed = True
                    else:
                        input("\nNo enemies to hammer!")
                        go_back = True
                        confirmed = True
                if not go_back:
                    self.battle_hammer(target)

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

    def auto_target(self, enemy_list):
        target = None
        for enemy in enemy_list:
            if enemy.special != "wings":
                return enemy
        return target

    def battle_jump(self, target):
        if target.special == "spike":
            input(f"\nMario jumps on {target.name}...")
            input("and lands right on the spike taking 1 damage to himself!")
            self.hp -= 1
        else:
            damage_calculation = self.jump.damage - target.defense
            input(f"\nMario jumps on {target.name} for {
                damage_calculation} damage")
            input(f"Mario jumps on {target.name} for {
                  damage_calculation} damage")
            target.hp -= damage_calculation * 2
            if target.hp <= 0:
                input(f"\n{target.name} has been eliminated")

    def battle_hammer(self, target):
        damage_calculation = self.hammer.damage - target.defense
        input(f"\nMario whacks {target.name} with a hammer for {
              damage_calculation} damage.")
        target.hp -= damage_calculation
        if target.hp <= 0:
            input(f"\n{target.name} has been eliminated")

    # Only ever used in the opening Crump Fight
    def opening_tutorial_turn(self, used_moves, enemy_list):
        go_back = True
        while go_back:
            go_back = False
            valid_command = False
            while not valid_command:
                print("")
                print("-----Mario's Turn-----")
                for move in self.moves_list:
                    i = self.moves_list.index(move) + 1
                    print(f"{i}. {move.name}")
                print("")
                command = input("Choose an action: ")
                if command.isdigit() and int(command) in [i for i in range(1, len(enemy_list) + 2)]:
                    valid_command = True
                    if int(command) == 1 and used_moves == ["jump"]:
                        print("\n" +
                              Colors.cyan + "Girl: Try out that big looking hammer instead, it probably packs a punch!" + Colors.reset)
                        input()
                        valid_command = False
                    if int(command) == 2 and used_moves == ["hammer"]:
                        print("\n" +
                              Colors.cyan + "Girl: Try out those heavy looking boots instead, they'll probably squish him!" + Colors.reset)
                        input()
                        valid_command = False
            if int(command) == 1:
                print("\nYou've selected jump!")
                target = self.target_selection(enemy_list)
                if target == "Go Back":
                    go_back = True
                else:
                    self.battle_jump(target)
                    move = "jump"
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
                if not go_back:
                    self.battle_hammer(enemy_list[0])
                move = "hammer"
        input()
        print("end of Mario's turn")
        return move
