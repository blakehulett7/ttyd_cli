from graphics import text_formatter, Colors
from battle_moves import body_slam
from logic import Mario, Enemy


def crump_opener():
    mario = Mario()
    crump = Enemy("Lord Crump", 5, 0, [body_slam])
    print(Colors.cyan + "Girl:")
    input()
    text_formatter("""Battle time, Mister Man! Just find a way to beat this freak of the week,
      OK? Don't sweat the details. Just jump on him or hit him with your
      hammer!""")
    while mario.hp != 0 and crump.hp != 0:
        print(mario)
        print(crump)
        mario.turn()

        input()


crump_opener()
