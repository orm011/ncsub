# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid means inorder traversal produces ordered set.
        prev = float('-inf')
        if root is None:
            return True

        stack = [(root, False)] # node, leftdone
        while stack:
            node, leftdone = stack.pop()
            if leftdone or (not node.left and not node.right):  
                # left is done, process midle
                if prev < node.val : # check order violation
                    prev = node.val
                    continue
                else:
                    return False # viol

            # stack is lifo, so 
            # need to go right -> middle -> left 
            if node.right is not None:
                stack.append((node.right, False))
            
            if node.left is not None:
                stack.append((node, True)) 
                stack.append((node.left, False))
            else:
                if prev < node.val:
                    prev = node.val
                else:
                    return False

        return True

        # space: 
        # stack will grow as the max depth of the tree, O(n)
        # time: 
        # go through each node at most twice: O(n)        