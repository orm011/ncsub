class UnionFind:
    def __init__(self):
        self.parents = {}

    def union(self, a: int, b: int) -> bool:
        # returns true if a union happened
        # post_condition: find(x) = find(y) 
        # for all x, y such that find(x) = find(a) and find(y) = find(b) before
        # the operations.
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        self.parents[pa] = pb
        return True

    def find(self, a: int) -> int: # returns class id for this element.
        # if element has never been in the structure, it will return its own value.
        path = [a]
        while True:
            if path[-1] not in self.parents:
                break
            else:
                curr = self.parents[path[-1]]
                path.append(curr)

        for p in path[:-1]: # compression
            self.parents[p] = path[-1]
        
        return path[-1]

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        ## kruskal strategy: 
        ## add edges greedily based on lowest weight except when they would 
        ## create a cycle.
        edges.sort(key=lambda e: e[-1], reverse=True)
        # print(f"{edges=}")
        total_weight = 0
        total_edges = 0
        components = UnionFind()

        while len(edges) > 0 and total_edges < (n - 1):
            (u, v, w) = edges.pop()
            if components.union(u, v):
                total_edges += 1
                total_weight += w
        
        return total_weight if total_edges == (n - 1) else -1