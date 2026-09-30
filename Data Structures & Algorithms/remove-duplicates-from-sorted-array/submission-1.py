class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0
        for n in nums:
            if n == prev:
                continue
            else:
                nums[k] = n
                k += 1
                prev = n

        del nums[k:]
        return k
