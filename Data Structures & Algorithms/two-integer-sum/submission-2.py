class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can we lower the complexity?
        # option A: sort-based.
        # option B: hash based.
        # build hash.
        # for each element, check if needed entry is present
        ## some issues. 
        ## we cannot reuse the same index, but the map will only store one entry per value, if the complement
        # equals the index, then it will find itself,
        # in that case we still want to return the right
        # value if there are two indices with the same value.
        num_map = {}
        for (i,n) in enumerate(nums):
            curr = num_map.get(n, set())
            curr.add(i)
            num_map[n] = curr # one to many map
        
        for (i,n) in enumerate(nums):
            complement = num_map.get(target - n, set())
            if i in complement:
                complement.remove(i) # remove itself

            if complement:
                return [i, min(complement)]
