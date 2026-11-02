"""Tests for the ``advanced`` module, run with pytest."""

import pytest

from advanced import mod, power, safe_sqrt


def test_power():
    """power returns base raised to exp."""
    assert power(2, 3) == 8


def test_mod():
    """mod returns the remainder of the division."""
    assert mod(10, 3) == 1


def test_safe_sqrt():
    """safe_sqrt returns the square root of a non-negative number."""
    assert safe_sqrt(16) == 4.0


def test_mod_by_zero_raises():
    """mod raises ValueError when the divisor is zero."""
    with pytest.raises(ValueError):
        mod(1, 0)


def test_safe_sqrt_negative_raises():
    """safe_sqrt raises ValueError for a negative number."""
    with pytest.raises(ValueError):
        safe_sqrt(-1)
