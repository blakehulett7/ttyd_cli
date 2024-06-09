from battle_moves import Move


class Game_Master:
    def __init__(self):
        self.room = "Rogueport Docks"


class Mario:
    def __init__(self):
        self.hp = 10
        self.fp = 5
        self.bp = 3
        self.defense = 0
        self.jump = Move("Jump", "Jump on an enemy", 1, True, False)
        self.hammer = Move(
            "Hammer", "Whack an enemy with your hammer", 2, False, True)
        self.moves_list = [self.jump, self.hammer]

    def __repr__(self):
        return f"(Mario! {self.hp} hp, {self.fp} fp, {self.bp} bp)"

    def turn(self, enemy_list):
        print("")
        print("-----Mario's Turn-----")
        for move in self.moves_list:
            i = self.moves_list.index(move) + 1
            print(f"{i}. {move.name}")
        print("")
        try:
            move_index = int(input("Choose an action: ")) - 1
            if 0 <= move_index < len(self.moves_list):
                selected_move = self.moves_list[move_index]
                print(selected_move.name)
                print("")
            else:
                print("\nInvalid selection, try again.")
                self.turn(enemy_list)
        except ValueError:
            print("Invalid selection, try again.")
            self.turn(enemy_list)

    def battle_jump(self, target):
        damage_calculation = self.jump.damage - target.defense
        input(f"Mario jumps on {target.name} for {damage_calculation} damage")
        input(f"Mario jumps on {target.name} for {damage_calculation} damage")


class Enemy:
    def __init__(self, name, hp, defense, moves_list, special=None):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.moves_list = moves_list
        self.special = special
        # Special will be spike, wings, or any other weird behaviors

    def __repr__(self):
        return f"({self.name}, {self.hp} hp, {self.defense} defense.)"
