

def action_menu_opener():
    print("-----ROGUEPORT DOCKS-----")
    print("1. Go into town")
    print("2. Save")
    action = input("What would you like to do? ")
    if action == "1":
        return
    elif action == "2":
        print("\nHA! There's no saving chump.")
        input()
        action_menu_opener()
    else:
        print("\nInvalid action, try again.")
        input()
        action_menu_opener()


def action_menu_prefight(gm):
    print(f"-----{gm.room}-----")
    print("1. Navigation")
    print("2. Tattle")
    print("3. Save")
    action = input("What would you like to do? ")
    if action == "1":
        return
    elif action == "2":
        input("\nDock Tattle")
        action_menu_prefight(gm)
    elif action == "3":
        print("\nHA! There's no saving chump.")
        input()
        action_menu_prefight(gm)
    else:
        print("\nInvalid action, try again.")
        input()
        action_menu_prefight(gm)
