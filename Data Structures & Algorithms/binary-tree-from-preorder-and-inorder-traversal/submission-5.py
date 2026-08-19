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
        
        dummy = TreeNode()
        stack.append((0, 0, len(preorder), dummy, False)) # dummy with left child.
        nodes = [TreeNode(val=v) for v in preorder] # will use all these nodes.

        while stack:
            (prestart, instart, k, parent, isleft) = stack.pop()
            #print(f"{prestart=}, {instart=}, {k=}, {parent.val=} {isleft=}")
            if k == 0:
                continue

            node = nodes[prestart]
            if isleft:
                parent.left = node
            else:
                parent.right = node
            
            if k == 1:
                continue    

            kprime = val2pos[node.val - min_val] - instart 
            # if val2pos[root] == instart, k = 0 for left side since empty.
            # represents this operaton on way back up.
            if kprime > 0: # already default to None, no need to deal with this case.
                stack.append((prestart+1, instart, kprime, node, True)) 
        
            if k - kprime - 1 > 0:
                stack.append((prestart+ kprime + 1, instart + kprime + 1, k - kprime - 1, node, False))
            # how does the return work. 
            # we need the state to return to a node that has the right root
            # eg, we know its None, or a single Node, where does it get assigned to its parent.
            # and how do we know where the parent is. 

        return dummy.right