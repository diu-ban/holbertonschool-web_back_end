#!/usr/bin/env python3
"""
This module define a function named index_range
that takes two integer arguments page and page_size.
"""

def index_range(page: int = 1, page_size: int = 1) -> tuple(int,int):
    start = (page - 1)*page_size
    end = page_size*page
    return (start,end)
