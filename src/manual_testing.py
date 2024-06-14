from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from logic import Game_Master
from partners import Goombella
from enemies import Goomba, Paragoomba


def main():
    gm = Game_Master()
    gm.partners.append(Goombella())
    gm.mario.paper_mode.append("airplane")
    gm.gamestate = 3
    gm.room = gm.room_list["Rogueport Sewers Entrance"]
    running = True
    while running:
        gm.debug_info()
        gm.room.check_gamestate(gm)
        gm.previous_room = gm.room
        gm.room.launch(gm)


main()
