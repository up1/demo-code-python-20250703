class Table:
    def __init__(self):
        self.slots = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]
    def draw(self):
        print("Current Table:")
        for row in self.slots:
            print(" | ".join(row))