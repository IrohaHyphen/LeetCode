# Accepted 12/10/2024
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = set()
        
        for num in arr:
            if num * 2 in numbers:
                return True
            
            if num % 2 == 0 and num / 2 in numbers:
                return True
            
            numbers.add(num)
        
        return False
