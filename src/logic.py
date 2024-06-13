from mario import Mario
from dialogue_rooms import Franklys_House, Suspicious_Room
from rooms import Room, Rogueport_Plaza, Rogueport_East
from rooms import Rogueport_Sewers_Entrance, Rogueport_Sewers_East_Corridor
from rooms import Rogueport_Sewers_Lower_Corridor, Thousand_Year_Door
from battle_moves import headbonk, spikebonk, dive


class Game_Master:
    def __init__(self):
        self.mario = Mario()
        self.partners = []
        self.room = "Rogueport Docks"
        self.gamestate = 1
        self.zess_t = False
        self.room_list = {
            "Rogueport Plaza": Rogueport_Plaza(),
            "Rogueport East": Rogueport_East(),
            "Frankly's House": Franklys_House(),
            "Rogueport Sewers": Rogueport_Sewers_Entrance(),
            "Entrance": Rogueport_Sewers_Entrance(),
            "East Corridor": Rogueport_Sewers_East_Corridor(),
            "Lower Corridor": Rogueport_Sewers_Lower_Corridor(),
            "Suspicious Doorway": Suspicious_Room(),
            "Thousand Year Door": Thousand_Year_Door()
        }

    def debug_info(self):
        print("\n", self.gamestate, self.room)
