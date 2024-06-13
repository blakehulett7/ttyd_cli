from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from logic import Mario, Enemy, Game_Master
from battle_moves import Enemy_Move


def main():
    gm = Game_Master()
    gm.gamestate = 3
    gm.room = gm.room_list["Rogueport East"]
    running = True
    while running:
        gm.check_special()
        gm.room.check_gamestate(gm)
        gm.room.launch(gm)


main()
