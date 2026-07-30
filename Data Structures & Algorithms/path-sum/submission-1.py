# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# lesson here: the base case was wrong. originally i made empty root return targetSum == 0,
# but this breaks with one-leaf nodes.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # approach: dfs exploration of tree tracking current sum
        def dfs(root, targetSum):
            if not root: # make it false always so nodes with single child check other value
                return False
            elif not root.left and not root.right:
                return targetSum == root.val
            
            # some child exists
            remainingSum = targetSum - root.val
            left_works = dfs(root.left, remainingSum)            
            if left_works:
                return True
            
            right_works = dfs(root.right, remainingSum)
            return right_works

        return dfs(root, targetSum)

        