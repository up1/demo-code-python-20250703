from table import Table

class Game:
    def __init__(self):
        self.table = Table()
        self.player = "x"
        self.status = "Play by "+ self.player

    def start(self):
        self.table.draw()

    def play(self, position):
        row = (position - 1) // 3
        col = (position - 1) % 3

        # Check if the position is valid
        if self.table.slots[row][col] != "-":
            self.status = "Invalid move! Position already taken."
            return False

        self.table.slots[row][col] = self.player
        self.table.draw()
        # Check win condition
        if self.check_win(self.player):
            print(f"{self.player} wins!")
            self.status = "The winner is "+ self.player
            return True

        # Switch player
        # self.player = "o" if self.player == "x" else "x"
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"
        self.status = "Play by "+ self.player

    def check_win(self, player):
        if all(self.table.slots[0][col] == player for col in range(3)):
           return True
        return False

# g1 = Game()
# g1.start()
# g1.play(1, "x")
# g1.play(2, "x")
# g1.play(3, "x")
# # X wins
# if g1.check_win("x"):
#     print("X wins")
# else:
#     print("No winner yet")