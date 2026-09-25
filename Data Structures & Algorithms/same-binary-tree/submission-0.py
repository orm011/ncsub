# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def equivalent(p, q) -> bool:
            if p is None or q is None:
                return p is None and q is None
            
            return (p.val == q.val and equivalent(p.left, q.left)
            and equivalent(p.right, q.right))

        return equivalent(p,q)