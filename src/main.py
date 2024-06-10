from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from battles import crump_opener
from action_menu import action_menu_opener
from logic import Mario, Enemy, Game_Master
from battle_moves import Enemy_Move
from rooms import Room


def main():
    gm = Game_Master()
    initialize_rooms()
    # Rogueport Docks
    opening_sequence()
    action_menu_opener()
    goombella_crump_sequence()
    mario = Mario()
    crump = Enemy("Lord Crump", 5, 0, [Enemy_Move("Body Slam", 1)])
    crump_opener(mario, crump)
    post_crump_opener()
    gm.room = rogueport_plaza
    plaza_entrance()
    gm.gamestate = 2
    running = True
    while running:
        gm.room.launch()


def initialize_rooms():
    rogueport_plaza = Room("Rogueport Plaza", ["Rogueport East"])
    rogueport_east = Room("Rogueport East", [
                          "Rogueport Plaza", "Frankly's House", "Merlin's House"
                          ],
                          None)


main()
