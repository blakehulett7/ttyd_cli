from battle_moves import jump, hammer


class Game_Master:
    def __init__(self):
        self.room = "Rogueport Docks"


class Mario:
    def __init__(self):
        self.hp = 10
        self.fp = 5
        self.bp = 3
        self.defense = 0
        self.moves_list = [jump, hammer]

    def __repr__(self):
        return f"(Mario! {self.hp} hp, {self.fp} fp, {self.bp} bp)"

    def turn(self):
        print("")
        print("-----Mario's Turn-----")
        for move in self.moves_list:
            i = self.moves_list.index(move) + 1
            print(f"{i}. {move.name}")
        print("")
        move_index = int(input("Choose an action: ")) - 1
        if 0 <= move_index < len(self.moves_list):
            selected_move = self.moves_list[move_index]
            print(selected_move.name)
            print("")
        else:
            print("\nInvalid selection, try again.")
            self.turn()


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
