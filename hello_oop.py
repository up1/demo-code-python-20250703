"""
Hello World in Python OOP
>>> hello = Hello("Somkiat")
>>> hello.sayHi()
'Hello, Somkiat'
"""


class Hello:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.age2ddddd = 1

    def sayHi(self) -> str:
        return "Hello, " + self.name


if __name__ == "__main__":
    import doctest

    doctest.testmod()
