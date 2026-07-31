class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smallest_idx = {}
        for (i,n) in enumerate(nums):
            if (target - n) in smallest_idx:
                return [smallest_idx[target - n ], i]
            
            if n not in smallest_idx: 
                smallest_idx[n] = i
            


