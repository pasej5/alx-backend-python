#!/usr/bin/env python3
"""
Type annotated function
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of mixed integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list.

    Returns:
        float: The sum of the elements in the mixed list.
    """
    return float(sum(mxd_lst))
