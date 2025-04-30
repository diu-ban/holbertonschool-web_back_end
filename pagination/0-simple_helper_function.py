#!/usr/bin/env python3
"""
This module define a function named index_range
that takes two integer arguments page and page_size.
"""

def index_range(page: int = 1, page_size: int = 1) -> (int,int):
    """
    Function return a tuple of 2
    containing a start index and an end
    index corresponding to the range of indexes
    """
    start = (page - 1)*page_size
    end = page_size*page
    return (start,end)
