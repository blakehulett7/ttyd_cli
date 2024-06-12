from mario import Mario
from enemies import Enemy
from rooms import Room, Franklys_House
from battle_moves import headbonk, spikebonk, dive
from battles import battle


class Game_Master:
    def __init__(self):
        self.mario = Mario()
        self.room = "Rogueport Docks"
        self.gamestate = 1
        self.zess_t = False
        self.room_list = {
            "Rogueport Plaza": Room("Rogueport Plaza", "rp_tattle", ["Rogueport East"], None, None),
            "Rogueport East": Room("Rogueport East", "re_tattle", [
                "Rogueport Plaza",
                "Frankly's House",
                "Merlin's House",
                "Ishnail Terriory",
                "Locked Gate"], None, None),
            "Frankly's House": Franklys_House(),
            "Rogueport Sewers": Room("Rogueport Sewers", "rs_tattle", ["d1", "d2", "pipe"], None, None)
        }

    def check_special(self):
        print(self.gamestate, self.room)
        if self.gamestate == 3 and self.room == self.room_list["Rogueport Sewers"]:
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
