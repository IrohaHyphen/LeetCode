# Accepted 12/10//2024
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        
        for i in range(len(str1)):
            # ord('a') + 1 = ord('b')
            if str1[i] == str2[j] or ord(str1[i]) + 1 == ord(str2[j]) or ord(str1[i]) - 25 == ord(str2[j]):
                j += 1
            
            if j == len(str2):
                return True
        
        return False
