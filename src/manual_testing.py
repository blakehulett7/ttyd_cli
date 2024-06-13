from cutscenes import opening_sequence, goombella_crump_sequence, post_crump_opener, plaza_entrance
from logic import Game_Master
from partners import Goombella


def main():
    gm = Game_Master()
    gm.partners.append(Goombella())
    gm.mario.paper_mode.append("airplane")
    gm.gamestate = 4
    gm.room = gm.room_list["Lower Corridor"]
    running = True
    while running:
        gm.debug_info()
        gm.room.check_gamestate(gm)
        gm.room.launch(gm)


main()
