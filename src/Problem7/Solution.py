# Accepted 12/6/2024

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        is_negative = False
        
        if x < 0:
            x = -x
            is_negative = True
        
        while x > 0:
            result += x % 10
            x //= 10
            if x > 0: result *= 10
        
        return 0 - result if is_negative else result
