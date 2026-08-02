# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is a good node if its value is greater than or equal to all above it.
        # ie, this depends on the max value above it. 
        # the count depends on what values below report.
        def dfs(node: Optional[TreeNode], prev_max: int) -> int:
            if not node:
                return 0
            curr_max = max(prev_max, node.val)
            left_good_nodes = dfs(node.left, curr_max)
            right_good_nodes = dfs(node.right, curr_max)
            current = 1 if node.val >= prev_max else 0
            return current + left_good_nodes + right_good_nodes

        return dfs(root, root.val)
            
