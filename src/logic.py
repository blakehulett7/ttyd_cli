from mario import Mario
from enemies import Enemy
from rooms import Room, Rogueport_Plaza, Rogueport_East, Franklys_House, Rogueport_Sewers_Entrance
from battle_moves import headbonk, spikebonk, dive
from battles import battle


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
            "Rogueport Sewers": Rogueport_Sewers_Entrance()
        }

    def check_special(self):
        print("\n", self.gamestate, self.room)
