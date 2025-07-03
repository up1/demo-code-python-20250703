def sayHi(name: str) -> str:
    """
    >>> sayHi("Somkiat")
    'Hello, Somkiat'
    >>> sayHi("World")
    'Hello, World'
    """
    return "Hello, " + name

if __name__ == "__main__":
    import doctest
    doctest.testmod()