# Accepted 12/6/2024
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        rows = [""] * numRows
        i = 0
        
        while i < len(s):
            # zigzag down part
            for j in range(numRows):
                if i < len(s):
                    rows[j] += s[i]
                    i += 1
            
            # zigzag up part
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    rows[j] += s[i]
                    i += 1
        
        for row in rows:
            result += row
        
        return result
