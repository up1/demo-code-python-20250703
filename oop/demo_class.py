class A:
    def __init__(self):
        print("Class A")
    
    def say(self):
        print("Hello from A")


class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")

    def say(self):
        super().say()
        print("Hello from B")

b = B()
b.say()