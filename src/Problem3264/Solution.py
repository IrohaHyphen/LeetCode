# Accepted 12/17/2024
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = [0] * len(nums)
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        
        for _ in range(k):
            x, i = heap[0]
            heapq.heapreplace(heap, (x * multiplier, i))
        
        for x, i in heap:
            result[i] = x
        
        return result
