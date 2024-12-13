# Accepted 12/13/2024
class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci
        memo = {1: 1, 2: 2}
        
        if n not in memo:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return memo[n]
