class Partner:
    def __repr__(self):
        return f"{self.name}, {self.hp} hp, {self.attack} attack, {self.defense} defense"

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


class Goombella(Partner):
    def __init__(self):
        self.name = "Goombella"
        self.hp = 10
        self.attack = 1
        self.defense = 0
        self.moves_list = ["Headbonk", "Tattle"]

    def turn(self, enemy_list):
        go_back = True
        while go_back:
            go_back = False
            command = "None"
            while not command.isdigit() or int(command) not in [i for i in range(1, len(enemy_list) + 2)]:
                print("")
                print("-----Goombella's Turn-----")
                for move in self.moves_list:
                    i = self.moves_list.index(move) + 1
                    print(f"{i}. {move}")
                print("")
                command = input("Choose an action: ")
            if int(command) == 1:
                print("\nYou've selected Headbonk!")
                target = self.target_selection(enemy_list)
                if target == "Go Back":
                    go_back = True
                else:
                    self.headbonk(target)
            if int(command) == 2:
                print("\nYou've selected Tattle!")
                target = self.target_selection(enemy_list)
                if target == "Go Back":
                    go_back = True
                else:
                    self.tattle(target)

        input("\nend of Goombella's turn")

    def headbonk(self, target):
        if target.special == "spike":
            input(f"\nGoombella jumps on {target.name}...")
            input("and lands right on the spike taking 1 damage to herself!")
            self.hp -= 1
        else:
            damage_calculation = self.attack - target.defense
            input(f"\nGoombella jumps on {target.name} for {
                damage_calculation} damage")
            input(f"Goombella jumps on {target.name} for {
                  damage_calculation} damage")
            target.hp -= damage_calculation * 2
            if target.hp <= 0:
                input(f"\n{target.name} has been eliminated")

    def tattle(self, target):
        print(f"\n--{target.name} Tattle--")
        input("\n(insert tattle description)")
        input(f"\nIt has {target.hp} health, an attack of {
              target.attack}, and a defense of {target.defense}.")
