from table import Table


class Game:
    def __init__(self):
        self.table = Table()

    def start(self):
        self.table.draw()

    def play(self, position, player):
        row = (position - 1) // 3
        col = (position - 1) % 3
        self.table.slots[row][col] = player
        self.table.draw()

    def check_win(self, player):
        if all(self.table.slots[0][col] == player for col in range(3)):
           return True
        return False

g1 = Game()
g1.start()
g1.play(1, "x")
g1.play(2, "x")
g1.play(3, "x")
# X wins
if g1.check_win("x"):
    print("X wins")
else:
    print("No winner yet")