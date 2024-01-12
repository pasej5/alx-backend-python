#!/usr/bin/env python3
"""
Type annotated function that takes float and returns a multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        its product with the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        returns a function that multiplies a float by multiplier.
        """
        return x * multiplier

    return multiplier_function
