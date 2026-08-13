"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # similar to graph copying, but we know all nodes are in a single path.
        # initial traversal: go through full list using next pointer. map old nodes to new nodes using a map (used to preserve referential consistency)
        # second traversal: all random pointers can now be replaced since all nodes exist.
        nodes = {}
        copy = None
        copy_tail = None
        orig_head = head

        while head:
            node = head
            head = head.next
            copy_node = Node(node.val)
            nodes[node] = copy_node
            if copy_tail:
                copy_tail.next = copy_node
                copy_tail = copy_node
            else: # first time.
                copy = copy_node
                copy_tail = copy_node

        for node,copy_node in nodes.items():
            copy_node.random = nodes.get(node.random)

        return copy