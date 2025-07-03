class Hello:
    def __init__(self, name):
        self.name = name

    def sayHi(self) -> str:
        return "Hello, " + self.name

if __name__ == "__main__":
    hello = Hello("Somkiat")
    print(hello.sayHi())