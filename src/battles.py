from graphics import text_formatter, Colors
from battle_moves import body_slam
from logic import Mario, Enemy


def crump_opener():
    print(Colors.cyan + "Girl:")
    input()
    text_formatter("""Battle time, Mister Man! Just find a way to beat this freak of the week,
      OK? Don't sweat the details. Just jump on him or hit him with your
      hammer!""")


def battle(mario, enemy_list):
    print(Colors.reset)
    while mario.hp != 0 and enemy_list != []:
        print(mario)
        for enemy in enemy_list:
            print(enemy)
        mario.turn(enemy_list)
        for enemy in enemy_list:
            if enemy.hp <= 0:
                enemy_list.remove(enemy)

        input()


mario = Mario()
crump = Enemy("Lord Crump", 5, 0, [body_slam])
battle(mario, [crump])
