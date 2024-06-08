def action_menu():
    print("-----ROGUEPORT DOCKS-----")
    print("1. Go into town")
    print("2. Save")
    action = input("What would you like to do? ")
    if action == "1":
        print("Starting crump goombella sequence...")
    elif action == "2":
        print("HA! There's no saving chump.")
    else:
        print("\nInvalid action, try again.")
        input()
        action_menu()
