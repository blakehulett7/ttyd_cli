from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from action_menu import action_menu_opener
from logic import Game_Master
from battle_moves import Enemy_Move
from mario import Mario


def main():
    gm = Game_Master()
    gm.room = gm.room_list["Rogueport Harbor"]
    gm.gamestate = 1
    running = True
    while running:
        gm.room.check_gamestate(gm)
        gm.room.launch(gm)


main()
