# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # idea: depth(t) = 1 if no children, 
        # or 1 + max(depth(child) for child in children)]
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), 
            self.maxDepth(root.right))
        
        