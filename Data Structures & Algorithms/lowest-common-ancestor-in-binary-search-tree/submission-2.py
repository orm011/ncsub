# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if there were parent pointers, then LCA would be
        # as simple as following parent pointers for both, while buildin up both paths until reaching root.
        # taking the first element in the intersection of these paths.
        # these operations would take time O(n), space O(n) 
        
        # This is a binary search tree though, which has extra constraints on relative positions
        # of p.val and q.val.
        # for example if we know the root value v, and p.val < root < q.val, 
        # then we can stop early, root is the answer.
        # ie, if we know p and q are transitive children of node, and if p.val < node.val < q.val, then node is their
        # LCA.
        
        # make p < q always.
        p, q = (p, q) if p.val < q.val else (q, p)

        node = root
        # p and q are not equal, but they could be equal to node.
        # since values are unique, can just handle it with \leq
        while True:
            if p.val <= node.val <= q.val: # includes case of lca being either one of the nodes.
                return node
            elif q.val < node.val:
                node = node.left
            else: # node.val < p.val
                node = node.right

        # O(n) time depending on depth
        # O(1) space: only track current node.
        






        