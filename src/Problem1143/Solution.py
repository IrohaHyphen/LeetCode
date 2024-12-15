# Accepted 12/17/2024
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # fill the matrix from the bottom right
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])
        
        return matrix[0][0]
