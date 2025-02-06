# Accepted 2/6/2025
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        valid_set = 0
        result_dict = dict()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key = nums[i] * nums[j]
                
                if key not in result_dict:
                    result_dict[key] = 0
                
                result_dict[key] += 1
                
                # new valid sets found
                if result_dict[key] >= 2:
                    valid_set += result_dict[key] - 1
        
        # there are 8 combinations of tuple for every valid set
        return valid_set * 8
