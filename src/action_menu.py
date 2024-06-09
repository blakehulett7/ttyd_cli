def action_menu():
    print("-----ROGUEPORT DOCKS-----")
    print("1. Go into town")
    print("2. Save")
    action = input("What would you like to do? ")
    if action == "1":
        return
    elif action == "2":
        print("\nHA! There's no saving chump.")
        input()
        action_menu()
    else:
        print("\nInvalid action, try again.")
        input()
        action_menu()
