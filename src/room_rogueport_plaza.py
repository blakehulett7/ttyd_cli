from logic import Game_Master
from action_menu import action_menu_prefight


def rogueport_plaza(gm):
    running = True
    while running:
        action_menu_prefight(gm)


gm = Game_Master()
gm.room = "Rogueport Plaza"
rogueport_plaza(gm)
