class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## go recursive here, if i have all permutations of a set of k elts 
        ## each position for the next element also generates a unique one
        if nums == []: # empty set yields single empty permutation.
            return [[]]

        h = nums[0]
        ans = []
        subperms = self.permute(nums[1:])
        for s in subperms:
            for i in range(len(s)+1): # k+1 fenceposts
                s1 = s.copy()
                s1.insert(i,h)
                ans.append(s1)
        return ans