from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from logic import Mario, Enemy, Game_Master
from battle_moves import Enemy_Move
from partners import Goombella


def main():
    gm = Game_Master()
    gm.partners.append(Goombella())
    gm.gamestate = 4
    gm.room = gm.room_list["Rogueport Sewers"]
    running = True
    while running:
        gm.check_special()
        gm.room.check_gamestate(gm)
        gm.room.launch(gm)


main()
