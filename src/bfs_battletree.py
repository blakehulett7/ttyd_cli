from graphics import Colors


class Battletree:
    def __init__(self):
        self.nil = Battlenode(None)
        self.root = Battlenode("Root")
        self.val = "Test"

    def __repr__(self):
        return f"{self.root}"

    def create_tree(self, mario, partner_list, enemy_list, current_node):
        partner = partner_list[0]
        formation = [mario, partner]
        if current_node == self.root:
            for good_guy in formation:
                self.root.children.append(Battlenode(good_guy))
        elif hasattr(current_node.val, "moves_list"):
            for move in current_node.val.moves_list:
                current_node.children.append(Battlenode(move))
        else:
            for enemy in enemy_list:
                current_node.children.append(Battlenode(enemy))
        for child in current_node.children:
            self.create_tree(mario, partner_list, enemy_list, child)


class Battlenode:
    def __init__(self, val):
        self.parent = None
        self.children = []
        self.val = val

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.val)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


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
                input(f"\nEnd of {good_guy.name}'s turn")
        for enemy in enemy_list:
            enemy.turn(formation)
    if enemy_list == []:
        input("\nVictory!")
        return True
    if mario.hp <= 0:
        input("\nGame Over")
        return False


def remove_dead_enemies(enemy_list):
    for enemy in enemy_list:
        if enemy.hp <= 0:
            enemy_list.remove(enemy)
            allies = enemy_list
            if hasattr(enemy, "death_event"):
                enemy.death_event(allies)
