from bfs_battletree import Battletree, Battlenode
from enemies import Goomba, Spiky_Goomba, Paragoomba
from partners import Goombella
from mario import Mario

mario = Mario()
goombella = Goombella()
enemies = [Goomba(), Spiky_Goomba(), Paragoomba()]
tree = Battletree()
tree.create_tree(mario, [goombella], enemies, tree.root)
print(tree)
