#!/usr/bin/env python3
"""A function that takes integers and floats and return the sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats and returns the
    sum of all the numbers in the list as float"""
    return sum(mxd_lst)
