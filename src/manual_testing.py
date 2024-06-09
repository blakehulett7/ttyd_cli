from cutscenes import opening_sequence, goombella_crump_sequence
from battles import crump_opener
from action_menu import action_menu
from logic import Mario, Enemy
from battle_moves import Enemy_Move


def main():
    mario = Mario()
    crump = Enemy("Lord Crump", 5, 0, [Enemy_Move("Body Slam", 1)])
    crump_opener(mario, crump)


main()
