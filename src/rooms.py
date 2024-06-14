import random
from enemies import Goomba, Spiky_Goomba, Paragoomba, Spinia, Blooper_Left, Blooper_Right, Blooper
from battles import battle


class Room:
    def __init__(self):
        self.enemies = None
        self.enemies_backup = None
        self.enemy_formations = None

    def __repr__(self):
        return f"{self.name}"

    def check_gamestate(self, gm):
        pass

    def launch(self, gm):
        action = self.action_menu()
        if action == "1":
            self.navigation(gm)
        if action == "2":
            self.fight(gm)
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
                    if "Paper Airplane to" in new_room_key:
                        new_room_key = new_room_key.replace(
                            "Paper Airplane to ", "")
                    if new_room_key not in gm.room_list:
                        input("\nNot Implemented Yet")
                    else:
                        gm.room = gm.room_list[new_room_key]
                        input(f"\nEntering {gm.room.name}")
                        self.enemies = self.enemies_backup

    def fight(self, gm):
        if self.enemies is None or self.enemies == []:
            input("\nNo enemies to fight")
            return
        go_back = False
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
                    go_back = True
                    print("")
                else:
                    enemy_index = int(target) - 1
                    target_enemy = self.enemies[enemy_index]
                    print(f"\nCall a battle on {target_enemy}")
                    victory = battle(gm.mario, gm.partners,
                                     self.enemy_formations[target_enemy])
        if not go_back:
            if victory:
                self.enemies.remove(target_enemy)

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
        if gm.gamestate >= 3 and "Locked Gate" in self.destinations:
            self.destinations.remove("Locked Gate")
            self.destinations.append("Pipe to Rogueport Sewers Entrance")


class Rogueport_Sewers_Entrance(Room):
    def __init__(self):
        self.name = "Rogueport Sewers: Entrance"
        self.description = "rs_tattle"
        self.destinations = [
            "Underground Town",
            "Pipe to East Corridor"]
        self.enemies = []
        self.enemies_backup = []
        self.enemy_formations = {"Spiky Goomba": [
            Spiky_Goomba(), Spiky_Goomba()]}

    def check_gamestate(self, gm):
        if gm.gamestate == 3:
            input("\nGoomba Bros Fight")
            enemies = [Goomba(), Spiky_Goomba(), Paragoomba()]
            battle(gm.mario, gm.partners, enemies)
            gm.gamestate += 1
        if gm.gamestate >= 5 and gm.previous_room != self:
            self.enemies.append("Spiky Goomba")
        if ("airplane" in gm.mario.paper_mode and
                "Paper Airplane to Flooded Room" not in self.destinations):
            self.destinations.append("Paper Airplane to Flooded Room")


class Flooded_Room(Room):
    def __init__(self):
        super().__init__()
        self.name = "Rogueport Sewers: Flooded Room"
        self.description = "rsf_tattle"
        self.destinations = ["Rogueport Sewers Entrance"]

    def check_gamestate(self, gm):
        if gm.gamestate == 5:
            input("\nBlooper fight here...")
            enemies = [Blooper_Left(), Blooper_Right(), Blooper()]
            battle(gm.mario, gm.partners, enemies)
            gm.gamestate += 1
            input("\nAn enticing grey pipe has appeared...")
            self.check_gamestate(gm)
        if gm.gamestate >= 6 and "Pipe to Petal Meadows" not in self.destinations:
            self.destinations.append("Pipe to Petal Meadows")


class Rogueport_Sewers_East_Corridor(Room):
    def __init__(self):
        self.name = "Rogueport Sewers: East Corridor"
        self.description = "rse_tattle"
        self.destinations = [
            "Pipe to Rogueport Sewers Entrance", "Pipe to Lower Corridor"]
        self.enemies = ["Goomba", "Spiky Goomba", "Paragoomba"]
        self.enemies_backup = ["Goomba", "Spiky Goomba", "Paragoomba"]
        self.enemy_formations = {
            "Goomba": [Goomba()],
            "Spiky Goomba": [Spiky_Goomba()],
            "Paragoomba": [Paragoomba()]
        }


class Rogueport_Sewers_Lower_Corridor(Room):
    def __init__(self):
        self.name = "Rogueport Sewers: Lower Corridor"
        self.description = "rsl_tattle"
        self.destinations = ["Pipe to East Corridor", "Suspicious Doorway"]
        self.enemies = ["Spinia", "Spinia"]
        self.enemies_backup = ["Spinia", "Spinia"]
        self.enemy_formations = {"Spinia": self.pick_formation()}
        # Known Bug: doesn't re-call the function when I pass the key for the second time.

    def check_gamestate(self, gm):
        if gm.previous_room == gm.room_list["East Corridor"]:
            input("\nUpon entering the room, a small grey creature notices you...")
            input("\nIt panics and crawls into a crack in the wall.")
        if ("airplane" in gm.mario.paper_mode and
                "Paper Airplane to Thousand Year Door" not in self.destinations):
            self.destinations.append("Paper Airplane to Thousand Year Door")

    def pick_formation(self):
        possible_formations = [
            [Spinia()],
            [Spinia(), Spinia()],
            [Spinia(), Spinia(), Spinia()],
            [Spinia(), Spinia(), Spinia(), Spinia()]
        ]
        index = random.randint(0, 3)
        return possible_formations[index]


class Thousand_Year_Door(Room):
    def __init__(self):
        self.name = "The Thousand Year Door"
        self.description = "ttyd_tattle"
        self.destinations = ["Lower Corridor"]
        self.enemies = None
        self.enemies_backup = None

    def check_gamestate(self, gm):
        if gm.gamestate == 4:
            input("\nFirst Door Cutscene...")
            gm.mario.special_moves.append("Sweet Treat")
            input("\nSweet Treat Unlocked!")
            input("\nBack at Frankly's House...")
            input("\nFrankly exposition")
            input("\nSweet Treat Tutorial goes here.")
            input(
                "\nFinally, Frankly tells us to go to Petal Meadows and we exit his house")
            input("\nAfter we leave, Frankly chases after us to give us a Power Smash.")
            input("\nInsert badge tutorial here")
            gm.gamestate += 1
            gm.room = gm.room_list["Rogueport East"]
            gm.room.check_gamestate(gm)
