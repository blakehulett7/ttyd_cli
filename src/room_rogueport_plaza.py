from logic import Game_Master
from action_menu import action_menu_prefight


def rogueport_plaza(gm):
    running = True
    while running:
        action_menu_prefight(gm)
        rp_navigation(gm)


def rp_navigation(gm):
    valid_action = False
    while not valid_action:
        destinations = ["Rogueport East", "Rogueport West",
                        "Back Alley", "Item Shop", "Inn", "Badge Shop"]
        if gm.zess_t:
            destinations.append("Zess T")
        destinations.append("Go Back")
        i = 1
        print("")
        print("-----Navigation-----")
        for dest in destinations:
            print(f"{i}. {dest}")
            i += 1
        action = input("Where would you like to go? ")
        if not action.isdigit() or int(action) not in [i for i in range(1, len(destinations) + 1)]:
            print("\ninvalid selection, try again.")
        else:
            if action == "1":
                valid_action = True
                print("\nstory progresses")
                gm.room = "Rogueport East"
                input()
            if action == "2":
                print("\nZess T sequence")
                input()
            if action in ["3", "4", "5", "6"]:
                print("\nnot implemented")
                input()
            if destinations[int(action) - 1] == "Zess T":
                print("\nnot implemented")
                input()
            if destinations[int(action) - 1] == "Go Back":
                print("\nGoing Back")
                print("")
                return
