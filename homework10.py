import random
import string
from typing import Optional


def generate_random_integer() -> int:
    """
    Generates a random integer between -10^10 and 10^10 (inclusive).

    Returns:
        int: A random integer between -10^10 and 10^10 (inclusive).
    """
    return random.randint(-10 ** 10, 10 ** 10)


def generate_random_string(length: Optional[int] = 10) -> str:
    """
    Generates a random string of lowercase letters of the given length.

    Args:
        length (int, optional): The length of the string to generate. Defaults to 10.

    Returns:
        str: A random string of lowercase letters of the given length.
    """
    if length < 1:
        raise ValueError("Length must be greater than or equal to 1.")
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
