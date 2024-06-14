from mario import Mario
from dialogue_rooms import Franklys_House, Suspicious_Room, Petal_Meadows
from rooms import Room, Rogueport_Plaza, Rogueport_East
from rooms import Rogueport_Sewers_Entrance, Rogueport_Sewers_East_Corridor, Flooded_Room
from rooms import Rogueport_Sewers_Lower_Corridor, Thousand_Year_Door
from battle_moves import headbonk, spikebonk, dive


class Game_Master:
    def __init__(self):
        self.mario = Mario()
        self.partners = []
        self.previous_room = None
        self.room = "Rogueport Docks"
        self.gamestate = 1
        self.zess_t = False
        self.room_list = {
            "Rogueport Plaza": Rogueport_Plaza(),
            "Rogueport East": Rogueport_East(),
            "Frankly's House": Franklys_House(),
            "Rogueport Sewers Entrance": Rogueport_Sewers_Entrance(),
            "Flooded Room": Flooded_Room(),
            "East Corridor": Rogueport_Sewers_East_Corridor(),
            "Lower Corridor": Rogueport_Sewers_Lower_Corridor(),
            "Suspicious Doorway": Suspicious_Room(),
            "Thousand Year Door": Thousand_Year_Door(),
            "Petal Meadows": Petal_Meadows()
        }

    def debug_info(self):
        print("\n", self.gamestate, self.room)
