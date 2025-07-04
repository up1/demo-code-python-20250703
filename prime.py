def find_number(number: int) -> [int]:
    """
    >>> find_number(2)
    [2]
    >>> find_number(4)
    [2, 2]
    >>> find_number(8)
    [2, 2, 2]
    """
    result = []
    divisor = 2
    while number%divisor==0:
        result.append(divisor)
        number = number / divisor

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()