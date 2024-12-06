class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        
        while True:
            cycle.add(n)
            n = sum((int(digit) ** 2 for digit in str(n)))
            
            if n == 1:
                return True
            
            if n in cycle:
                return False
