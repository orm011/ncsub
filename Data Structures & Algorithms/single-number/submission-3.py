class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # now with O(1) space complexity.
        # cannot build a separate set.
        total = 0
        for n in nums:
            total ^= n

        return total


