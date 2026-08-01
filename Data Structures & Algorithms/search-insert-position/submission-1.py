class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target <= n: # will return at the first opportunity
                return i

        return len(nums)
        