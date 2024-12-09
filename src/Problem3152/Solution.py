# Accepted 12/9/2024
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        
        for query in queries:
            result.append(True) if is_special(nums, query) else result.append(False)
        
        return result


def is_special(array: List[int], constraint: List[int]) -> bool:
    for i in range(constraint[0], constraint[1]):
        # if the sum is even, the two numbers have the same parity (even/odd)
        if (array[i] + array[i + 1]) % 2 == 0:
            return False
    
    return True
