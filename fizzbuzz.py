def say(number: int) -> str:
    """
    >>> say(1)
    '1'
    >>> say(2)
    '2'
    >>> say(3)
    'Fizz'
    >>> say(4)
    '4'
    >>> say(5)
    'Buzz'
    >>> say(6)
    'Fizz'
    >>> say(7)
    '7'
    >>> say(8)
    '8'
    >>> say(9)
    'Fizz'
    >>> say(15)
    'FizzBuzz'
    """
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

if __name__ == "__main__":
    import doctest
    doctest.testmod()