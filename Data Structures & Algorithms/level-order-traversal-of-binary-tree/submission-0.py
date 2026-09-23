# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breadth first search gets the right order down,
        # but need separation into levels.
        if not root:
            return []
        
        queue = deque([(root, 0)])
        
        prevlevel = -1
        output = []
        # track level using the integer
        while queue:
            head, level = queue.popleft()
            if level != prevlevel: # new with one element
                output.append([head.val])
            else: # existing list
                output[-1].append(head.val)

            if head.left:
                queue.append((head.left, level + 1)) 
            # left first so that 2 before 3
            if head.right:
                queue.append((head.right, level + 1))

            prevlevel = level

        return output



        