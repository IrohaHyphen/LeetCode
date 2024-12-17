# Accepted 12/17/2024
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = ""
        sorted_letters = sorted(list(s))
        counter = 0
        
        for i in range(len(sorted_letters) - 1, -1, -1):
            if i + 1 < len(sorted_letters) and sorted_letters[i] == sorted_letters[i + 1]:
                counter += 1
                
                if counter > repeatLimit:
                    # there is no next distinct letter
                    if sorted_letters[i] == sorted_letters[0]:
                        return result
                    
                    # find the next distinct letter
                    for j in range(i - 1, -1, -1):
                        if sorted_letters[i] != sorted_letters[j]:
                            counter = 0
                            result += sorted_letters[j]
                            sorted_letters[i], sorted_letters[j] = sorted_letters[j], sorted_letters[i]
                
                else:
                    result += sorted_letters[i]
            
            else:
                counter = 1
                result += sorted_letters[i]
        
        return result
