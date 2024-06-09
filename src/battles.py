from graphics import text_formatter, Colors
from battle_moves import body_slam
from logic import Mario, Enemy


def crump_opener(mario, crump):
    print(Colors.cyan + "Girl:")
    input()
    text_formatter("""Battle time, Mister Man! Just find a way to beat this freak of the week,
      OK? Don't sweat the details. Just jump on him or hit him with your
      hammer!""")
    battle(mario, [crump])


def battle(mario, enemy_list):
    print(Colors.reset)
    while mario.hp != 0 and enemy_list != []:
        print(mario)
        for enemy in enemy_list:
            print(enemy)
        input()
        mario.turn(enemy_list)
        input()
        for enemy in enemy_list:
            if enemy.hp <= 0:
                enemy_list.remove(enemy)
        for enemy in enemy_list:
            enemy.turn(mario)

        input()
