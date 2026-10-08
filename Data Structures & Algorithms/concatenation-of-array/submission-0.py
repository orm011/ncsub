class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None for _ in range(2*n)]
        for i in range(2*n):
            ans[i] = nums[i % n]
        return ans
        