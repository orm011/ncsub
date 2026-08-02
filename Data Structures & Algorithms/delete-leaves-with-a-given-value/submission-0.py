# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfsremove(root, target):
            if root is None:
                return None

            # process children first
            root.left = dfsremove(root.left, target)
            root.right = dfsremove(root.right, target)

            # single leaf node with matching value 
            # deletes itself
            if root.left is None and root.right is None:
                if root.val == target:
                    return None

            return root
        
        return dfsremove(root, target)