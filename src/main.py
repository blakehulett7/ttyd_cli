from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from action_menu import action_menu_opener
from logic import Game_Master
from battle_moves import Enemy_Move
from mario import Mario


def main():
    gm = Game_Master()
    # Rogueport Docks
    action_menu_opener()
    goombella_crump_sequence()
    mario = Mario()
    crump = Enemy("Lord Crump", 5, 0, [Enemy_Move("Body Slam", 1)])
    crump_opener(mario, crump)
    post_crump_opener()
    gm.room = gm.room_list["Rogueport Plaza"]
    plaza_entrance()
    gm.gamestate = 2
    running = True
    while running:
        gm.check_special()
        gm.room.launch(gm)


main()
