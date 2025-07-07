class Table:
    def __init__(self):
        self.slots = [["o", "-", "-"], 
                      ["-", "x", "-"],
                      ["-", "-", "x"]]

    def draw(self):
        print("Current Table:")
        for row in self.slots:
            print(" | ".join(row))

x = Table()
x.draw()
x.slots[0][1] = "x"
x.draw()
x.slots[2][1] = "o"
x.draw()