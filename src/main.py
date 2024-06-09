from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener
from battles import crump_opener
from action_menu import action_menu
from logic import Mario, Enemy, Game_Master
from battle_moves import Enemy_Move


def main():
    gm = Game_Master()
    # Rogueport Docks
    opening_sequence()
    action_menu()
    goombella_crump_sequence()
    mario = Mario()
    crump = Enemy("Lord Crump", 5, 0, [Enemy_Move("Body Slam", 1)])
    crump_opener(mario, crump)
    post_crump_opener()
    gm.room = "Rogueport Plaza"


main()
