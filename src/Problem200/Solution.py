# Accepted 12/13/2024
# BFS
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j))
                    
                    # BFS
                    while queue:
                        i, j = queue.popleft()
                        
                        # north neighbor
                        if i > 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
                            visited.add((i - 1, j))
                            queue.append((i - 1, j))
                        # east neighbor
                        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1" and (i, j + 1) not in visited:
                            visited.add((i, j + 1))
                            queue.append((i, j + 1))
                        # south neighbor
                        if i < len(grid) - 1 and grid[i + 1][j] == "1" and (i + 1, j) not in visited:
                            visited.add((i + 1, j))
                            queue.append((i + 1, j))
                        # west neighbor
                        if j > 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
                            visited.add((i, j - 1))
                            queue.append((i, j - 1))
                    
                    result += 1
        
        return result

# DFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         result = 0
#         visited = set()
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     visited.add((i, j))
#                     dfs(i, j, grid, visited)
#                     result += 1
#
#         return result
#
#
# def dfs(i, j, grid, visited):
#     # north neighbor
#     if j > 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
#         visited.add((i, j - 1))
#         dfs(i, j - 1, grid, visited)
#     # east neighbor
#     if i < len(grid) - 1 and grid[i + 1][j] == "1" and (i + 1, j) not in visited:
#         visited.add((i + 1, j))
#         dfs(i + 1, j, grid, visited)
#     # south neighbor
#     if j < len(grid[0]) - 1 and grid[i][j + 1] == "1" and (i, j + 1) not in visited:
#         visited.add((i, j + 1))
#         dfs(i, j + 1, grid, visited)
#     # west neighbor
#     if i > 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
#         visited.add((i - 1, j))
#         dfs(i - 1, j, grid, visited)
