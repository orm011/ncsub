# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the longest path may either go through root, 
        # or it is fully contained within the left or right children trees.
        # if it goes through root, then it must be made up of the longest path
        # from root down for both left and right. 
        def dfs(root: Optional[TreeNode]) -> tuple[int, int]:
            """ returns both the diameter of this tree node, as well as
            the longest path length starting from root"""
            if root is None:
                return (0, 0)
            # elif root.left is None and root.right is None:
            #     return (0, 0) # also 0 depth, 0 diam.
            right_diam, right_depth = dfs(root.right)
            left_diam, left_depth = dfs(root.left)

            if root.right is not None:
                right_depth += 1 # account for edge to root
            if root.left is not None:
                left_depth += 1 # account for edge to root

            diam = max(left_diam, right_diam, left_depth + right_depth)
            depth = max(left_depth, right_depth)
            return (diam, depth)

        (diam, _) = dfs(root)
        return diam
        