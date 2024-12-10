# Accepted 12/10/2024
class Solution:
    def maximumLength(self, s: str) -> int:
        current_best = -1
        substrings = {}
        
        for i in range(len(s)):
            current_substring = s[i]
            
            # 1 character substrings
            if current_substring in substrings:
                substrings[current_substring] += 1
            else:
                substrings[current_substring] = 1
            
            # if occurs thrice
            if substrings[current_substring] == 3:
                current_best = max(current_best, len(current_substring))
            
            # 2 or more characters substrings
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    current_substring += s[j]
                else:
                    break
                
                if current_substring in substrings:
                    substrings[current_substring] += 1
                else:
                    substrings[current_substring] = 1
                
                # if occurs thrice
                if substrings[current_substring] == 3:
                    current_best = max(current_best, len(current_substring))
        
        return current_best
