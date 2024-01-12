#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list
"""


from typing import List



def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)

