class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## option A: recursion. pick one element and then enumerate all subsets below, return each 
        ## with and without the element.
        ## option B: iterate through numbers, up to 2^n each bit encodes whether an element is or is not.
        ## going for option A
        if nums == []:
            return [[]]

        first = nums[0]
        ans = []
        for subset in self.subsets(nums[1:]):
            nofirst = subset
            yesfirst = [first] + subset
            ans += [nofirst, yesfirst]
        
        return ans
        