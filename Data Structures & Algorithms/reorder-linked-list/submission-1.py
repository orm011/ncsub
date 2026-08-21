# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next

        # if list is even length, 2n
        # will point at position n, the sta (0 based) 
        # eg, 2. slow points at position 1.
        # if list is odd length, loop is similar to 2n+2:
        # except final pointer does not move. so will be at position n+1

        # reverse second part:
        endoffirst = slow 
        reverse = None
        while slow:
            # build the list from last node backward.
            tmp = slow.next
            # prepend first elt to tail
            slow.next = reverse
            reverse = slow
            slow = tmp
        

        # ptnode = reverse
        # while ptnode:
        #     print(f"{ptnode.val=}{ptnode.next is None=}")
        #     ptnode = ptnode.next
        # return
        # head still points to all before.

        tail = ListNode(-1) # dummy
        while reverse:
            print(f"{head.val=} {reverse.val=} {tail.val=} ")
            tail.next = head
            tail = tail.next
            head = head.next


            tail.next = reverse
            tail = tail.next
            reverse = reverse.next


        # once reverse is done. 
        # recall head is not going to have a null pointer. 
        if head.next == endoffirst:
            tail.next = head
            tail = tail.next
            head = head.next

        assert head == endoffirst
        tail.next = None # close it.
            
        

