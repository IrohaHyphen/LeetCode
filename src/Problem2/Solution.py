# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Accepted 12/5/2024
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            tail.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            
            tail = tail.next
        
        return dummy_head.next
