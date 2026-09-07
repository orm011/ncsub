# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ### root is always there.
        ## there is always one node per level, the right most one
        ## option 1: depth first going 
        # first right then left works if we track
        ## when we have seen a depth before.
        ## in that case: at each node, we track its depth, and if 
        ## it is above any seen before, then we must be the rightmost
        ## for that level (as long as we always go right child first)
        ## another option is breadth first search, where we add nodes right to left, and track heights. need a queue and need to track depth 
        # also.

        maxlevel = -1
        output = []
        def dfs(root, level) -> None:
            nonlocal maxlevel
            if root is None:
                return 
            
            if level > maxlevel:
                output.append(root.val)
                maxlevel += 1
            
            dfs(root.right, level+1)
            dfs(root.left, level+1)
        
        dfs(root, 0)
        return output