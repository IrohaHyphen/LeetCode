# Accepted 12/19/2024
import heapq
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        
        heap = [(x, i) for i, x in enumerate(arr)]
        heapq.heapify(heap)
        
        current_index = 0
        
        while heap:
            value, index = heapq.heappop(heap)
            
            if index > current_index:
                current_index = index
                result += 1
        
        return result
