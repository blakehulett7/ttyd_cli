class Room:
    def __init__(self, name, destinations, enemies):
        self.name = name
        self.destinations = destinations
        self.enemies = enemies

    def launch(self):
        action = self.action_menu()
        if action == "1":
            self.navigation()

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

    def navigation(self):
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
                print("Valid selection")
                valid_dest = True
                if dest == options[-1]:
                    print("")
                else:
                    dest_index = int(dest) - 1
                    gm.room = self.destinations[dest_index]


rp = Room("Rogueport East", [
    "Rogueport Plaza", "Frankly's House", "Merlin's House"
], None)
rp.launch()
