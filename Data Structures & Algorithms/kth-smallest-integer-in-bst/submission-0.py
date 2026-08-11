# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if the tree is not balanced, or if we dont know the number
        # of child nodes left and right of a node, we need to visit the
        # first k nodes in dfs left to right (with the parent visited in the middle)
        
        num_visited = 0
        value = None
        def dfs(root, k) -> bool: # return bool when done
            nonlocal num_visited
            nonlocal value

            if root is None:
                return False
            done = dfs(root.left,k)
            if done:
                return True
            num_visited += 1 # count center 
            if num_visited == k:
                value = root.val
                return True
            return dfs(root.right, k)
            
        dfs(root,k)
        return value

            
            

        