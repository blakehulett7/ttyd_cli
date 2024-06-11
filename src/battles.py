from graphics import text_formatter, Colors
from battle_moves import body_slam, headbonk, spin
from logic import Mario, Enemy


def crump_opener(mario, crump):
    print(Colors.cyan + "Girl:")
    input()
    text_formatter("""Battle time, Mister Man! Just find a way to beat this freak of the week,
      OK? Don't sweat the details. Just jump on him or hit him with your
      hammer!""")
    used_moves = []
    while crump.hp > 0:
        print(Colors.reset)
        print(mario)
        print(crump)
        input()
        used_moves.append(mario.opening_tutorial_turn(used_moves, [crump]))
        input()
        if used_moves == ["jump"]:
            print(Colors.cyan +
                  "Girl: Nice Move! Try whacking him with that hammer next.")
            input()
        if used_moves == ["hammer"]:
            print(
                Colors.cyan + "Girl: Way to bop him! Try jumping on him with those heavy boots next.")
            input()
        print(Colors.reset)
        if crump.hp > 0:
            crump.turn(mario)
        else:
            print("-----END OF BATTLE-----")
            print("Mario has defeated Lord Crump!")
            mario.star_points += 9
            print(
                f"Mario gets 9 star points for a total of {mario.star_points}!")
        input()


def battle(mario, enemy_list):
    print(Colors.reset)
    while mario.hp > 0 and enemy_list != []:
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


mario = Mario()
goomba = Enemy("Goomba", 2, 0, [headbonk])
spinia = Enemy("Spinia", 3, 0, [spin])
battle(mario, [goomba, spinia])
