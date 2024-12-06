# Accepted 12/6/2024
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        result = 0
        
        banned_set = set(banned)
        total = 0
        
        for i in range(1, n + 1):
            if i not in banned_set and total + i <= maxSum:
                total += i
                result += 1
        
        return result
