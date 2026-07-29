# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        # idea, while one list is smaller than or equal, keep getting the nodes and 
        # prepending to result.
        # each prepend is O(1)
        # final result is the reverse list.

        rev_result = []
        while ptr1 and ptr2:
            while ptr1 and ptr2 and ptr1.val <= ptr2.val:
                rev_result.append(ptr1.val)
                ptr1 = ptr1.next
            while ptr1 and ptr2 and ptr1.val > ptr2.val:
                rev_result.append(ptr2.val)
                ptr2 = ptr2.next

        while ptr1: # ptr2 must be None
            rev_result.append(ptr1.val)
            ptr1 = ptr1.next
        
        while ptr2:
            rev_result.append(ptr2.val)
            ptr2 = ptr2.next

        head = None
        while rev_result:
            val = rev_result.pop()
            head = ListNode(val=val, next=head)
        return head


        

