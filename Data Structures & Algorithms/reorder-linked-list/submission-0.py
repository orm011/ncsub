# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # the early part of the list depends on reading values 
        # in the tail of the list, which can only be known after traversing.
        # but once we use the last pointer, we need to back off to the previous.
        # node 0 maps to node n-1.
        # idea with extra space: stack.
        # traverse list left to right, add elements do a deque
        
        nodes = deque([])
        ptr = head
        while ptr:
            # print(f"{ptr=} {c=}")
            nodes.append(ptr)
            ptr = ptr.next

        tail = nodes.popleft()
        while len(nodes) > 1:
            last = nodes.pop()
            first = nodes.popleft()
            
            tail.next = last
            last.next = first

            tail = first
        
        # handle last node if any
        if nodes:
            tail.next = nodes.pop()
            tail = tail.next

        tail.next = None

