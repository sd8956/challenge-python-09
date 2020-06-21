"""Challenge-python-09"""
from typing import List

class Solution:
    """Funcion que duplica los ceros en una lista"""
    def duplicate_zeros(self, arr: List[int]):
        zeros = 0
        last = 0
        len_arr = len(arr)

        for idx, value in enumerate(arr):
            if value == 0 and idx + zeros <= len_arr - 1:
                zeros += 1
                last = idx
    
        idx = len_arr - 1
        for _ in arr:
            if zeros > 0:
                arr[idx] = arr[idx - zeros]
                if arr[idx - zeros] == 0 and idx - zeros <= last:
                    idx -= 1
                    arr[idx] = 0
                    zeros -= 1           
            idx -= 1
