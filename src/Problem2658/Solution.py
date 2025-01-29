# Accepted 1/29/2025
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        current_max = 0
        overall_max = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    visited.add((i, j))
                    current_max += grid[i][j]
                    current_max = dfs(grid, i, j, visited, current_max)
                    
                    # next segment
                    overall_max = max(overall_max, current_max)
                    current_max = 0
        
        return overall_max


def dfs(grid, i, j, visited, current_max) -> int:
    # explore north
    if j > 0 and (i, j - 1) not in visited and grid[i][j - 1] > 0:
        visited.add((i, j - 1))
        current_max += grid[i][j - 1]
        current_max = dfs(grid, i, j - 1, visited, current_max)
    
    # explore east
    if i < len(grid) - 1 and (i + 1, j) not in visited and grid[i + 1][j] > 0:
        visited.add((i + 1, j))
        current_max += grid[i + 1][j]
        current_max = dfs(grid, i + 1, j, visited, current_max)
    
    # explore south
    if j < len(grid[0]) - 1 and (i, j + 1) not in visited and grid[i][j + 1] > 0:
        visited.add((i, j + 1))
        current_max += grid[i][j + 1]
        current_max = dfs(grid, i, j + 1, visited, current_max)
    
    # explore west
    if i > 0 and (i - 1, j) not in visited and grid[i - 1][j] > 0:
        visited.add((i - 1, j))
        current_max += grid[i - 1][j]
        current_max = dfs(grid, i - 1, j, visited, current_max)
    
    return current_max
