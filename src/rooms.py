class Room:
    def __init__(self, name, description, destinations, enemies, enemy_formations):
        self.name = name
        self.description = description
        self.destinations = destinations
        self.enemies = enemies
        self.enemies_backup = enemies
        self.enemy_formations = enemy_formations

    def __repr__(self):
        return f"{self.name}"

    def launch(self, gm):
        action = self.action_menu()
        if action == "1":
            self.navigation(gm)
        if action == "2":
            self.fight()
        if action == "3":
            self.tattle()
        if action == "4":
            self.save()

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
                    if "Pipe to" in new_room_key:
                        new_room_key = new_room_key.replace("Pipe to ", "")
                    if new_room_key not in gm.room_list:
                        input("\nNot Implemented Yet")
                    else:
                        gm.room = gm.room_list[new_room_key]
                        input(f"\nEntering {gm.room.name}")
                        self.enemies = self.enemies_backup

    def fight(self):
        if self.enemies is None or self.enemies == []:
            input("\nNo enemies to fight")
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
        input("\n" + self.description)

    def save(self):
        input("\nHA! There's no saving chump!")


class Shop_Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def launch(self):
        pass


class Dialogue_Room:
    def __init__(self, name, character, dialogue_list, adjacent_room):
        self.name = name
        self.character = character
        self.adjacent_room = adjacent_room
        self.dialogue_list = dialogue_list
        self.counter = 0

    def launch(self, gm):
        dialogue = self.dialogue_list[self.counter]
        input("\n" + dialogue)
        if self.counter == 0:
            self.counter += 1
        gm.room = gm.room_list[self.adjacent_room]

    def increment_counter(self):
        self.counter += 1


class Rogueport_Plaza(Room):
    def __init__(self):
        self.name = "Rogueport Plaza"
        self.description = "re_tattle"
        self.destinations = ["Rogueport East"]
        self.enemies = None
        self.enemies_backup = None
        self.enemy_formations = None

    def check_gamestate(self, gm):
        pass


class Rogueport_East(Room):
    def __init__(self):
        self.name = "Rogueport East"
        self.description = "re_tattle"
        self.destinations = [
            "Rogueport Plaza",
            "Frankly's House",
            "Merlin's House",
            "Ishnail Terriory",
            "Locked Gate"]
        self.enemies = None
        self.enemies_backup = None
        self.enemy_formations = None

    def check_gamestate(self, gm):
        if gm.gamestate >= 3:
            self.destinations.remove("Locked Gate")
            self.destinations.append("Pipe to Rogueport Sewers")


class Franklys_House:
    def __init__(self):
        self.name = "Frankly's House"
        self.dialogue_list = ["frankly intro dialogue"]

    def __repr__(self):
        return f"{self.name}"

    def check_gamestate(self, gm):
        pass

    def launch(self, gm):
        if gm.gamestate == 2:
            input("\n" + self.dialogue_list[0])
            input("\nProfessor Frankly has joined your party!")
            input("\nFrankly gate unlock dialogue")
            input("\nRogueport Sewer pipe unlocked!")
            gm.gamestate += 1
        elif gm.gamestate in [4, 5]:
            input("\nProfessor Frankly: No time to dawdle, let's head through the pipe!")
        else:
            input("\nGamestate Error")
        gm.room = gm.room_list["Rogueport East"]
