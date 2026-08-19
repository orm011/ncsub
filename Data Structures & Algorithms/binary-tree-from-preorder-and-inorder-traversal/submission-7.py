# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # try same as sol 4 but without the stack problem
        # option 1. use a stack data structure to track subproblem.
        # what do we do to the return value?
        # we can add it to a result stack also.
        stack = [] # will hold: prestart, instart, and k (length), parent, and isleft
        value_range = [min(preorder), max(preorder)]
        min_val = value_range[0]
        val2pos = [-1 for _ in range(value_range[1] - min_val + 1)]
        for i,val in enumerate(inorder):
            val2pos[val - min_val] =  i
        
        stack.append((0, 0, len(preorder))) # dummy with left child.
        nodes = [TreeNode(val=v) for v in preorder] # will use all these nodes.

        while stack:
            (prestart, instart, k) = stack.pop()
            #print(f"{prestart=}, {instart=}, {k=}, {parent.val=} {isleft=}")
            node = nodes[prestart]
            
            if k == 1:
                continue    

            kprime = val2pos[node.val - min_val] - instart 
            # if val2pos[root] == instart, k = 0 for left side since empty.
            # represents this operaton on way back up.
            if kprime > 0: # already default to None, no need to deal with this case.
                node.left = nodes[prestart + 1]
                if kprime > 1:
                    stack.append((prestart + 1, instart, kprime)) 
        
            if k - kprime - 1 > 0:
                node.right = nodes[prestart + kprime + 1]
                if k - kprime - 1 > 1:
                    stack.append((prestart + kprime + 1, instart + kprime + 1, k - kprime - 1))
            # how does the return work. 
            # we need the state to return to a node that has the right root
            # eg, we know its None, or a single Node, where does it get assigned to its parent.
            # and how do we know where the parent is. 

        return nodes[0]