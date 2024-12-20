from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_queue = deque([[root, 0]])
        to_be_reversed = deque()
        
        # BFS
        while node_queue:
            node, level = node_queue.popleft()
            
            # when the level is odd, gather the nodes that will be reversed
            if level % 2 == 1:
                to_be_reversed.append(node)
            # when the level turns even, execute the reversal of the previous level
            else:
                while to_be_reversed:
                    current_left = to_be_reversed.popleft()
                    current_right = to_be_reversed.pop()
                    current_left.val, current_right.val = current_right.val, current_left.val
            
            # BFS
            if node.left:
                node_queue.append([node.left, level + 1])
            if node.right:
                node_queue.append([node.right, level + 1])
        
        # if the tree ends at an odd level
        while to_be_reversed:
            current_left = to_be_reversed.popleft()
            current_right = to_be_reversed.pop()
            current_left.val, current_right.val = current_right.val, current_left.val
        
        return root
