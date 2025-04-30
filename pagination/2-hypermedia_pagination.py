#!/usr/bin/env python3
"""
This module define a function named index_range
that takes two integer arguments page and page_size.
"""

import csv
import math
from typing import List

def index_range(page: int = 1, page_size: int = 1) -> (int,int):
    """
    Function return a tuple of 2
    containing a start index and an end
    index corresponding to the range of indexes
    """
    start = (page - 1)*page_size
    end = page_size*page
    return (start,end)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            try:
                assert isinstance(page,int) and page > 0
                assert isinstance(page_size, int) and page_size > 0
            except:
                 return []

            dataset = self.dataset()
            start, end = index_range(page, page_size)

            if start >= len(dataset):
                 return []
            return dataset[start:end]
    
    def get_hyper(self, page: int=1, page_size:int=10) -> {str,any}:
        data = self.get_page(page, page_size)
        data_len = len(self.dataset())
        total_page = math.ceil(data_len / page_size)

        return {
             "page_size":len(data),
             "page":page,
             "data":data,
             "next_page":page + 1 if (page * page_size)<data_len else None,
             "prev_page":page - 1 if page > 1 else None,
             "total_page":total_page
        }

    
