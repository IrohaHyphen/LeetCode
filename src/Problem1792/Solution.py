# Accepted 12/17/2024
import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        
        for i in range(len(classes)):
            good, total = classes[i][0], classes[i][1]
            heapq.heappush(heap, [-improvement(good, total), good, total])
        
        for _ in range(extraStudents):
            good, total = heap[0][1], heap[0][2]
            heapq.heapreplace(heap, [-improvement(good + 1, total + 1), good + 1, total + 1])
        
        result = 0.0
        
        for _, good, total in heap:
            result += good / total
        
        result /= len(heap)
        
        return result


def improvement(good: int, total: float) -> float:
    return (good + 1) / (total + 1) - (good / total)
