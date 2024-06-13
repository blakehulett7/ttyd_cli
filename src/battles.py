from graphics import text_formatter, Colors
from battle_moves import body_slam, headbonk, spin
from mario import Mario
from enemies import Enemy


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


def battle(mario, partner_list, enemy_list):
    print(Colors.reset)
    while mario.hp > 0 and enemy_list != []:
        print(mario)
        print(partner_list[0])
        print("--------------------------")
        for enemy in enemy_list:
            print(enemy)
        input()
        selected_partner = partner_list[0]
        if selected_partner.hp > 0:
            valid_formation = False
            while not valid_formation:
                print("\n--Your Turn--")
                print("1. Mario")
                print(f"2. {selected_partner.name}")
                answer = input("Who would you like to go first? ")
                if answer == "1":
                    formation = [mario, selected_partner]
                    valid_formation = True
                elif answer == "2":
                    formation = [selected_partner, mario]
                    valid_formation = True
                else:
                    input("\nInvalid selection, try again")
        else:
            formation = [mario]
        for good_guy in formation:
            if enemy_list != []:
                good_guy.turn(enemy_list)
                remove_dead_enemies(enemy_list)
        for enemy in enemy_list:
            enemy.turn(mario)
    if enemy_list == []:
        input("\nVictory!")
        return True
    if mario.hp <= 0:
        input("\nGame Over")
        return False

        input()


def remove_dead_enemies(enemy_list):
    for enemy in enemy_list:
        if enemy.hp <= 0:
            enemy_list.remove(enemy)
