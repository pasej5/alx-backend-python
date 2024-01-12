#!/u
# r/bin/env python3
"""
 type-annotated function to_kv that takes a string
 k and an int OR float
"""


from typing import Tuple


def to_kv(k: str, v: any) -> Tuple[str, any]:
    """Converts key-value pair to a tuple.

    Args:
        k (str): The key.
        v (any): The value.

    Returns:
        Tuple[str, any]: A tuple containing the key and value.
    """
    return (k, v)
