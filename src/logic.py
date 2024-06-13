from mario import Mario
from enemies import Enemy
from rooms import Room, Rogueport_Plaza, Rogueport_East, Franklys_House
from battle_moves import headbonk, spikebonk, dive
from battles import battle


class Game_Master:
    def __init__(self):
        self.mario = Mario()
        self.room = "Rogueport Docks"
        self.gamestate = 1
        self.zess_t = False
        self.room_list = {
            "Rogueport Plaza": Rogueport_Plaza(),
            "Rogueport East": Rogueport_East(),
            "Frankly's House": Franklys_House(),
            "Rogueport Sewers": Room("Rogueport Sewers: Entrance", "rs_tattle", [
                "Underground Town",
                "Pipe to East Corridor",
                "pipe"], None, None)
        }

    def check_special(self):
        print("\n", self.gamestate, self.room)
        if self.gamestate == 4:
            if self.room == self.room_list["Rogueport Sewers"]:
                input("\nGoomba Bros Fight")
                enemies = [
                    Enemy("Goomba", 2, 0, [headbonk]),
                    Enemy("Spiky Goomba", 2, 0, [spikebonk], "spike"),
                    Enemy("Paragoomba", 2, 0, [dive], "wings")
                ]
                battle(self.mario, enemies)
                self.gamestate += 1


def tattle(room):
    print(f"\n{room} Tattle")
