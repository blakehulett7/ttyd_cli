from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from logic import Mario, Enemy, Game_Master
from battle_moves import Enemy_Move


def main():
    gm = Game_Master()
    gm.room = gm.room_list["Rogueport Plaza"]
    running = True
    while running:
        gm.room.launch(gm)


main()
