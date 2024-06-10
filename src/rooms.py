class Room:
    def __init__(self, name, destinations, enemies):
        self.name = name
        self.destinations = destinations
        self.enemies = enemies

    def action_menu(self):
        valid_action = False
        while not valid_action:
            print(f"-----{self.name}-----")
            print("1. Navigation")
            print("2. Fight")
            print("3. Tattle")
            print("4. Save")
            action = input("What would you like to do? ")
            if action not in ["1", "2", "3", "4"]:
                print("\nInvalid action, try again!")
            else:

    def navigation(self):
        print("-----Navigation-----")
        i = 1
        for dest in self.destinations:
            print(f"{i}. {dest}")
            i += 1
        print(f"{i}. Go Back")


rp = Room("Rogueport East", [
    "Rogueport Plaza", "Frankly's House", "Merlin's House"
], None)
rp.action_menu()
