# Accepted 12/24/2024
import heapq
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        pending_queries = [[] for _ in range(len(heights))]
        
        for i, q in enumerate(queries):
            alice, bob = q
            # Bob is always the further one
            if bob < alice:
                alice, bob = bob, alice
            
            # if they are already on the same building
            if bob == alice:
                result[i] = bob
                continue
            
            # if they can meet at Bob's building
            if heights[alice] < heights[bob]:
                result[i] = bob
                continue
            
            # if they need to find another building
            pending_queries[bob].append((heights[alice], i))
        
        min_heap = []
        
        # iterate through all buildings
        for i in range(len(heights)):
            # add queries to the heap when their Bob is on the current building
            # to make sure that we will only check buildings further than their Bob
            while pending_queries[i]:
                heapq.heappush(min_heap, pending_queries[i].pop())
            
            # if the current building is higher than their Alice's building
            while min_heap and min_heap[0][0] < heights[i]:
                height, index = heapq.heappop(min_heap)
                result[index] = i
        
        return result
