# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        def bfs():
            prev = -1
            if root is None:
                return 
            q = deque([(root, 0)])
            while q:
                (node, level) = q.popleft()
                if level > prev:
                    prev = level
                    output.append(node.val)
                
                if node.right is not None:
                    q.append((node.right, level + 1))
                
                if node.left is not None:
                    q.append((node.left, level + 1))

            return output

        bfs()
        return output


        