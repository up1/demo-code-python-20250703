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

    def reset(self):
        self.table = Table()
        self.start()


g1 = Game()
g1.start()
g1.play(1, "x")
g1.play(2, "o")
g1.play(3, "x")
g1.play(4, "o")
g1.play(5, "x")
g1.play(6, "o")
g1.play(7, "x")
g1.play(8, "o")
g1.play(9, "x")
