# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        step = head
        while step and step.next:
            if step.val == step.next.val:
                step.next = step.next.next
            else:
                step = step.next
        return head
