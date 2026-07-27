# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This particular solution will not materialize a recursive structure.
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        from collections import deque
        self.root = root
        self.stack = deque()
        # idea: keep a pointer to the current node, and a boolean on whether its pre or post.
        # more fleshed out: there is a natural order to the full tree, no need to keep state for each level etc.
        # we just need to keep pointers: which node are we returning next.
        # once we return it, which would be the next one. this requires going up to the parent.
        # how do we know which parent it was if there is no pointer?
        if self.root:
            self.stack.append((self.root, "pre"))
    
    def next(self) -> int:
        # example: null root: error, has next would have worked.
        # example: single element, null left and right, pre becomes post, return value.

        next_node, node_state = self.stack.pop() 
        while node_state == "pre":
            # insert right, middle, then left so that left goes first
            if next_node.right:
                self.stack.append((next_node.right, "pre"))
            
            self.stack.append((next_node, "post"))
            
            if next_node.left:
                self.stack.append((next_node.left, "pre"))

            # now go to the next one
            next_node, node_state = self.stack.pop() 
        else: # this is the middle
            return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()