# Accepted 12/20/2024
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(prices) - 1):
            while stack and stack[-1][0] >= prices[i]:
                stack_price, stack_index = stack.pop()
                prices[stack_index] -= prices[i]
            
            if prices[i] >= prices[i + 1]:
                prices[i] -= prices[i + 1]
            else:
                stack.append([prices[i], i])
        
        return prices
