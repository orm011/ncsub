class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # the sum of xor totals of all subsets
        # option 1: enumerate all subsets, compute each xor, add to running total.
        # runtime: each element is seen 2^n-1 times, xored that many times.
        # total of O(n * 2 ^n) operations.
        # we do have 2^n subsets, each with its own xor total, unclear you can do better than that        
        def level_helper(nums: list[int]) -> list[int]:
            """returns the xor totals for all subsets in this array"""
            if nums == []:
                return [0]
            first = nums[-1]
            partials = level_helper(nums[:-1])
            totals = [p for p in partials] + [p^first for p in partials]
            return totals

        all_xors = level_helper(nums)
        return sum(all_xors)
        # space: O(2^n) entries for the partials
        # time: O(n * 2*n) operations        

