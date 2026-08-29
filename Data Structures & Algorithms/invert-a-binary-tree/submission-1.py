# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        def rec(root) -> Optional[TreeNode]:
            # we invert each subtree, then replace the left and right nodes.
            if root is None:
                return None
            
            newright = rec(root.left)
            newleft = rec(root.right)
            root.left = newleft
            root.right = newright
            return root
        
        # this will have generated a new tree, with full memory allocations
        return rec(root)