import math

class Node:
    def __init__(self, val, left, right, depth):
        self.val = val
        self.left = left
        self.right = right
        self.depth = depth

    def _repr_helper(self) -> list:
        acc = [self.val, self.left._repr_helper() if self.left else None, self.right._repr_helper() if self.right else None]
        return acc

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self._repr_helper())

class MinHeap:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def _help_push(self, val: int, node: Node):
        if node.val >= val:
            new_val = node.val
            node.val = val
        else:
            new_val = val

        # insert bigger element under
        if node.left is None:
            node.left = Node(new_val, None, None, 1)
        elif node.right is None:
            node.right = Node(new_val, None, None, 1)
        elif node.right.depth <= node.left.depth:
            self._help_push(new_val, node.right)
        else:
            self._help_push(new_val, node.left)

        node.depth = max(node.left.depth if node.left else 0, node.right.depth if node.right else 0) + 1

    def _help_pop(self, node: Node) -> (int, Optional[Node]): 
        """returns a value and a node to replace the original one, which could be None at this point)"""
        # print(f"help pop: {node=} {node.left=} {node.right}")
        ret_value = node.val
        if not node.left and not node.right:
            return (ret_value, None)
        elif not node.left and node.right:
            return (ret_value, node.right)
        elif node.left and not node.right:
            return (ret_value, node.left)
        else:
            # have left and right children, in that case we want to pop the deeper one.
            # we need the new value to preserve the heap property. smaller at the top.
            left_val, new_left = self._help_pop(node.left)
            # print(f"{new_left=}")
            right_val, new_right = self._help_pop(node.right)
            #  print(f"{new_right=}")

            node.left = new_left
            node.right = new_right

            new_val, other_val = (left_val, right_val) if left_val <= right_val else (right_val, left_val)
            node.val = new_val
            self._help_push(other_val, node) # move other value if necessary to keep branches balanced.

        return ret_value, node

    def push(self, val: int) -> None:
        if not self.root:
            self.root = Node(val, None, None, depth=1)
            return
        self._help_push(val, self.root)
        # print(self)

    def pop(self) -> int:
        if not self.root:
            return -1

        val, node = self._help_pop(self.root)
        self.root = node
        # print(self)

        return val

    def top(self) -> int:
        return self.root.val if self.root else -1
        

    def heapify(self, nums: List[int]) -> None:
        for n in nums:
            self.push(n)
        
        