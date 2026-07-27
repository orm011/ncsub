class UnionFind:
    def __init__(self):
        # for every node, holds a pointer to another within the same class.
        # root nodes do not point to anything.
        self.parents = {}
        # for every "root" node, holds the size of its underlying tree.
        self.component_sizes: dict[int, int] = {}
        self.max_size = 1

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

        # need to update size map. if not in map yet, its size 1 (itself only)
        size_eq1 = self.component_sizes.get(eq1,1)
        size_eq2 = self.component_sizes.get(eq2,1)

        self.component_sizes[eq1] = size_eq1 + size_eq2
  
        if eq2 in self.component_sizes: # remove non root.
            del self.component_sizes[eq2]

        self.max_size = max(self.component_sizes[eq1], self.max_size)

        return False

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## solution idea. 
        ## the equivalence classes are sets of elements forming consecutive chains
        ## Q: how do we create the structure? what do we iterate? what do we union?
        ## once we have the structure, we need to return the size of the largest component.
        ## to track this number, we will modify the union find to track total sizes as we union components
        data = UnionFind()
        actual_nums = set(nums)
        for num in actual_nums:
            if num + 1 in actual_nums:
                data.union(num, num+1)

        if not nums:
            return 0

        return data.max_size




        