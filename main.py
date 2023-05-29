"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    a = string
    b = a.upper()
    c = b.count('A')
    d = b.count('E')
    e = b.count('I')
    f = b.count('O')
    g = b.count('U')
    return(c+d+e+f+g)

    

