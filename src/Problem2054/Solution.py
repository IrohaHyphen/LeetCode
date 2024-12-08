# Accepted 12/8/2024
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        possible_values = set()
        
        # if attend two events
        for i in range(len(events)):
            for j in range(i + 1, len(events)):
                if events[i][1] < events[j][0] or events[j][1] < events[i][0]:
                    possible_values.add(events[i][2] + events[j][2])
        
        # if attend one event
        for event in events:
            possible_values.add(event[2])
        
        return max(possible_values)
