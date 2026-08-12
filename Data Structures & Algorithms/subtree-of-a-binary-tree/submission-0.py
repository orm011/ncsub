# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## the subroot could match potentially any node within root.
# one approach: traverse the root graph and pick out every possible starting node
# then, for each, try traversing it simultaneously with subroot.
# this takes O(R) to create that initial graph,
# then O(S) to match/unmatch each with S: O(R*S)
# extra space here: O(R) for all the pointers to all R nodes.

## can interleave these searches, saving up the R space. still need to have a
# queue or a stack for the matches.
# there are two sets of state: the current root traversal for starting nodes,
# and the current match of startgin from current starting node with S.

## alternative approach: start by matching leaves? if leaves match build up.
## start with a queue of leaves for S. for each, find them in the set of leaves of root, and add the pair to the queue. (there could be multiple matches)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_match(root, subRoot): # match both recursively
            if root is None and subRoot is None:
                return True
            elif subRoot is None or root is None:
                return False
            elif root.val != subRoot.val:
                return False
            else:
                return ( dfs_match(root.left, subRoot.left) and
                    dfs_match(root.right, subRoot.right) )

        # traverse main root looking for matching locations
        def dfs_main(root: Optional[TreeNode]) -> bool:
            if dfs_match(root, subRoot):
                return True
            elif root is None:
                return False
            else:
                return (dfs_main(root.left) or dfs_main(root.right))
        
        # eg. empty root. matches empty subroot.
        return dfs_main(root)