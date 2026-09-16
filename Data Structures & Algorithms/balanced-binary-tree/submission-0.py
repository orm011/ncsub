# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced: left and right for every node differ by at most 1.
        def rec(node) -> (int, bool): # do the work for each node,
        # but also return info needed
            if not node:
                return (0, True)

            lheight, lbalance = rec(node.left)
            rheight, rbalance = rec(node.right)

            if not lbalance or not rbalance:
                return (None, False) # dont bother further computing. 
                
            return ( max(lheight, rheight) + 1, 
                    abs(lheight - rheight) <= 1)
        
        (_, ans) = rec(root)
        return ans