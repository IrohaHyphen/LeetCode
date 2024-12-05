class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_char_index = 0
        target_char_index = 0
        
        while start_char_index < len(start) and target_char_index < len(target):
            while start[start_char_index] == '_':
                start_char_index += 1
            while target[target_char_index] == '_':
                target_char_index += 1
            
            if start[start_char_index] != target[target_char_index]:
                # if nth char of start and target are different
                return False
            if start[start_char_index] == 'L' and target_char_index > start_char_index:
                # if nth L of target is to the right of nth L of start
                return False
            if start[start_char_index] == 'R' and target_char_index < start_char_index:
                # if nth R of target is to the left of nth R of start
                return False
            
            start_char_index += 1
            target_char_index += 1
        
        return True
