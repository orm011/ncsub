class ListNode:
    def __init__(self, key: int = -1, prev: Option['ListNode'] = None, 
    next: Option['ListNode'] = None):
        self.key = key
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.key=} {self.prev is None =} {self.next is None =}"

    def __str__(self):
        return self.__repr__()

class LRUCache:

    def __init__(self, capacity: int):
        self.values = {} # key -> (value, ListNode)
        
        self.head = ListNode(key=-1)
        self.tail = ListNode(key=-2)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def traverse(self):
        node = self.head
        vals = []
        while node is not None:
            vals.append(node.key)
            nextnode = node.next
            assert nextnode is None or nextnode.prev == node, f"{nextnode.prev=} {node.key=}"
            node = node.next
        return vals

    def print_state(self):
        print(f"{self.values=} {self.capacity=} {self.traverse()=}")

    def _move_to_tail(self, node: ListNode):
        if node.next == self.tail:
            return 

        # need to: fix nodes' two pointers, fix tail prev pointer, fix old neighbors.
        oldprev = node.prev # preserve before writing
        oldnext = node.next

        oldtailprev = self.tail.prev

        node.prev = oldtailprev
        node.next = self.tail
        self.tail.prev = node
        oldtailprev.next = node

        # node has been moved now. but its old neighbors need repair,
        # unless node had no prev and no next
        if oldprev is not None and oldnext is not None:
            oldprev.next = oldnext
            oldnext.prev = oldprev
        
    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        ans, node = self.values[key]
        self._move_to_tail(node)
        return ans

    def put(self, key: int, value: int) -> None:
        # if the key is already here,
        # only need to move to front.
        val = self.values.get(key, None)
        # self.print_state()
        # handle list update
        if val is not None:
            ans, node = val
            self._move_to_tail(node)
        elif len(self.values) == self.capacity:
            node = self.head.next # will re-use the node we would evict
            del self.values[node.key]
            node.key = key # re-use node
            self._move_to_tail(node) # move to front.
        else: 
            node = ListNode(key=key)
            self._move_to_tail(node) # handles new node case

        # update map
        self.values[key] = (value, node)
