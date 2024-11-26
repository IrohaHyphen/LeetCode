// Accepted 11/26/2024
package Problem2;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result;
        ListNode dummyHead = new ListNode(0);
        ListNode tail = dummyHead;
        int carry = 0;
        
        while (true) {
            if (l1 == null && l2 == null && carry == 0) {
                result = dummyHead.next;
                break;
            }
            
            int firstValue;
            
            if (l1 != null) {
                firstValue = l1.val;
                l1 = l1.next;
            } else {
                firstValue = 0;
            }
            
            int secondValue;
            
            if (l2 != null) {
                secondValue = l2.val;
                l2 = l2.next;
            } else {
                secondValue = 0;
            }
            
            tail.next = new ListNode((firstValue + secondValue + carry) % 10);
            carry = (firstValue + secondValue + carry) / 10;
            
            tail = tail.next;
        }
        
        return result;
    }
}

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    
    ListNode() {
    }
    
    ListNode(int val) {
        this.val = val;
    }
    
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
