from action_menu import action_menu_prefight


def rogueport_east(gm):
    running = True
    while running:
        action_menu_prefight(gm)
        re_navigation(gm)


def re_navigation(gm):
    valid_action = False
    while not valid_action:
        destinations = ["Rogueport Plaza", "Frankly's House", "Merlin's House"]
        if gm.gamestate > 2:
            destinations.append("Warp Pipe")
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
                print("\nGoing back to Rogueport Plaza")
                input()
                gm.room = "Rogueport Plaza"
            if action == "2":
                print("\nstory progresses")
                input()
                rogueport_east(gm)
            if action == "3":
                print("\nNot Implemented")
                input()
            if destinations[int(action) - 1] == "Go Back":
                print("\nGoing Back")
                print("")
                return
