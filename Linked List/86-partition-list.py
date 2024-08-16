from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        l = []
    
        # main function 
        step = head
        while step:
            if step.val < x:
                l.append(step.val)
            step = step.next
        
        curr = head
        while curr:
            if curr.val >= x:
                l.append(curr.val)
            curr = curr.next
        
        node = ListNode()
        temp = node
        for ele in l:
            temp.next = ListNode(val=ele)
            temp = temp.next
    
        return node.next
        
