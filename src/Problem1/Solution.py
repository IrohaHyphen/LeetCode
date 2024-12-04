# Accepted 12/4/2024
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_number = 0
        second_number = 0
        
        numbers = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in numbers:
                first_number = numbers[complement]
                second_number = i
                break
            
            numbers[nums[i]] = i
        
        return [first_number, second_number]
