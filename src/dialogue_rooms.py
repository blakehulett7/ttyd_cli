class Suspicious_Room:
    def __init__(self):
        self.name = "Suspicious Room"

    def __repr__(self):
        return f"{self.name}"

    def check_gamestate(self, gm):
        pass

    def launch(self, gm):
        if "airplane" not in gm.mario.paper_mode:
            input("\n(1st Chest Cutscene here, no key required...)")
            input("\nAirplane Mode Unlocked!")
            gm.mario.paper_mode.append("airplane")
        else:
            input("\nThere's just a suspicious looking open chest...")
        gm.room = gm.room_list["Lower Corridor"]


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


class Petal_Meadows:
    def __init__(self):
        self.name = "Petal Meadows"

    def __repr__(self):
        return f"{self.name}"

    def check_gamestate(self, gm):
        pass

    def launch(self, gm):
        input("\n-----END OF PROLOGUE-----")
