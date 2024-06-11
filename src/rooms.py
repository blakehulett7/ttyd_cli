class Room:
    def __init__(self, name, desciption, destinations, enemies, enemy_formations, special=None):
        self.name = name
        self.desciption = desciption
        self.destinations = destinations
        self.enemies = enemies
        self.enemies_backup = enemies
        self.enemy_formations = enemy_formations
        self.special = special

    def launch(self, gm):
        if self.special is None:
            action = self.action_menu()
            if action == "1":
                self.navigation(gm)
            if action == "2":
                self.fight()
            if action == "3":
                self.tattle()
            if action == "4":
                self.save()
        else:
            input("Special Room")

    def action_menu(self):
        valid_action = False
        while not valid_action:
            print("")
            print(f"-----{self.name}-----")
            print("1. Navigation")
            print("2. Fight")
            print("3. Tattle")
            print("4. Save")
            action = input("What would you like to do? ")
            if action not in ["1", "2", "3", "4"]:
                input("\nInvalid action, try again!")
            else:
                return action

    def navigation(self, gm):
        valid_dest = False
        while not valid_dest:
            options = []
            print("")
            print("-----Navigation-----")
            i = 1
            for dest in self.destinations:
                print(f"{i}. {dest}")
                options.append(f"{i}")
                i += 1
            options.append(f"{i}")
            print(f"{i}. Go Back")
            dest = input("Where would you like to go? ")
            if dest not in options:
                input("\nInvalid destination, try again")
            else:
                valid_dest = True
                if dest == options[-1]:
                    print("")
                else:
                    dest_index = int(dest) - 1
                    new_room_key = self.destinations[dest_index]
                    if new_room_key not in gm.room_list:
                        input("\nNot Implemented Yet")
                    else:
                        gm.room = gm.room_list[new_room_key]
                        self.enemies = self.enemies_backup

    def fight(self):
        if self.enemies is None or self.enemies == []:
            print("\nNo enemies to fight")
            return
        valid_enemy = False
        while not valid_enemy:
            options = []
            print("")
            print("-----Fight-----")
            i = 1
            for enemy in self.enemies:
                print(f"{i}. {enemy}")
                options.append(f"{i}")
                i += 1
            options.append(f"{i}")
            print(f"{i}. Go Back")
            target = input("Who would you like to fight? ")
            if target not in options:
                input("\nInvalid destination, try again")
            else:
                valid_enemy = True
                if target == options[-1]:
                    print("")
                else:
                    enemy_index = int(target) - 1
                    target_enemy = self.enemies[enemy_index]
                    print(f"Call a battle on {target_enemy}")

    def tattle(self):
        print("\n" + self.desciption)

    def save(self):
        print("\nHA! There's no saving chump!")
