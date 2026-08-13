# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        output = ListNode() # dummy
        tail = output
        carry = 0
        while l1 or l2 or carry > 0:
            # need to account for any left over nodes or carry
            # must end only when all are accounted for.

            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            total = l1val + l2val + carry
            tail.next = ListNode(val=total % 10)
            tail = tail.next
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return output.next

        



        