class UnionFind:
    def __init__(self):
        self.parents = {}

    def find(self, key: int) -> int:
        """ returns an equivalence class for this key by traversing to find a root. 
        if the key is not in the structure, it returns its value """
        lookup_key = key
        while lookup_key in self.parents:
            lookup_key = self.parents[lookup_key]

        return lookup_key 

    def union(self, key1: int, key2: int) -> bool:
        """ unions the equivalence classes for both. returns True if already equivalent.
            if the keys are not yet in the structure, it adds them.
        """
        eq1 = self.find(key1)
        eq2 = self.find(key2)
        if eq1 == eq2:
            return True

        # point eq class for second to eq1
        self.parents[eq2] = eq1
        return False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## idea: we union on each edge. ensuring both nodes are part of the same root.
        ## when, in order to actually count components, we can find each vertex and add to set.
        ## any left over vertices not seen in any edges, we add at the end.
        data = UnionFind()
        for (src,dst) in edges:
            data.union(src,dst)

        distinct_components = set()
        for i in range(n):
            cid = data.find(i)
            distinct_components.add(cid)

        return len(distinct_components)


        