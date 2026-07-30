# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order traversal. 
        # how is it different from pre-order traversal 
        # or post order traversal.
        # left node << node << right node.
        # does this extend to arbitrary graph? eg ternary tree. what's the order?

        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return [*left, root.val, *right]
