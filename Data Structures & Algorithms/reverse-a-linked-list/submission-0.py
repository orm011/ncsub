# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # approach 1:
        # can keep an in progress list: as we see values we prepend them
        # time O(n) space O(n) if making a new list.
        # if we allow ourselves destroying the input, can we reduce space by mutation?  
        # the first node will change its next pointer to null, need to read the next
        # before using. but after that no need to look at it again.

        output = None
        while head:
            curr = head # cell
            head = head.next # read the pointer 
            curr.next = output # prepend
            output = curr # keep track.

        return output

            

        