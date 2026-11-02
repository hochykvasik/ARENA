"""Advanced math helpers.

A small collection of arithmetic utilities with explicit error handling.
"""

import math


def power(base, exp):
    """Raise ``base`` to the power ``exp``.

    Args:
        base (int | float): The number to be raised.
        exp (int | float): The exponent.

    Returns:
        int | float: The value of ``base ** exp``.

    Examples:
        >>> power(2, 10)
        1024
        >>> power(9, 0.5)
        3.0
    """
    return base ** exp


def mod(a, b):
    """Return the remainder of the division of ``a`` by ``b``.

    Args:
        a (int | float): The dividend.
        b (int | float): The divisor. Must not be zero.

    Returns:
        int | float: The value of ``a % b``.

    Raises:
        ValueError: If ``b`` is zero.

    Examples:
        >>> mod(7, 3)
        1
        >>> mod(1, 0)
        Traceback (most recent call last):
        ...
        ValueError: Division by zero
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a % b


def safe_sqrt(x):
    """Return the square root of ``x``.

    Args:
        x (int | float): A non-negative number.

    Returns:
        float: The value of ``math.sqrt(x)``.

    Raises:
        ValueError: If ``x`` is negative.

    Examples:
        >>> safe_sqrt(16)
        4.0
        >>> safe_sqrt(-1)
        Traceback (most recent call last):
        ...
        ValueError: Cannot calculate square root of a negative number
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)
