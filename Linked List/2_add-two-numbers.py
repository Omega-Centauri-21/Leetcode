# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None

        summ = carry
        if l1:
            summ += l1.val
            l1 = l1.next
        if l2:
            summ += l2.val
            l2 = l2.next

        result = ListNode( summ % 10)
        result.next = self.addTwoNumbers(l1, l2, summ // 10)
        return result
