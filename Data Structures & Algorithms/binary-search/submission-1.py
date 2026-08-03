class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2 # can equal l. always less than r
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid


        # at this point l == r
        return l if nums[l] == target else -1