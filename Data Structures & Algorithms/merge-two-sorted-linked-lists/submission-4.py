# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # destructive solution that modifies the input lists.
        # no extra space.
        output_list = None
        # we will re-use the memory structures but modify pointers.


        ptr1 = list1
        ptr2 = list2
        # tricky: making sure we are modifying the pointers in the right sequence
        # so that we can continue traversing the old remaining lists
        # while at the same time modifying its cells.
        # key: only modify a cell which won't be used anymore.

        head_node = ListNode()
        prev_node = head_node # just a non-null place holder
        while ptr1 and ptr2:
            val1 = ptr1.val
            val2 = ptr2.val
            if val1 <= val2: # use ptr1 cell
                prev_node.next = ptr1
                ptr1 = ptr1.next
            elif val2 < val1:
                prev_node.next = ptr2
                ptr2 = ptr2.next

            # last node is now modified
            prev_node = prev_node.next

        # ptr2 is done. then,
        # connect to whatever remains of list1. 
        if not ptr2:
            prev_node.next = ptr1
        elif not ptr1:
            prev_node.next = ptr2
        
        # always not empty
        return head_node.next

            

        