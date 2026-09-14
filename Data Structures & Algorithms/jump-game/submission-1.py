class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # obs. 
        # we can always jump unless we must go through a 0 node.
        # eg, if there are no 0, answer is true always.
        # if there is a single 0 at position i, answer is true if 
        # there is any preceding position j < i such that nums[j] > i - j 
        # (if equal, then it will land right on the 0)
        # imaging attempting this left to right in one pass.
        # we can track largest preceding position, but each forward step
        # decreases its usefulness by one, so that a newer position may be better even if smaller. lets cal 

        best = 0
        n = len(nums)
        for i in range(n-1): # exclude last index, include 0
            best -= 1
            best = max(best, nums[i])
            if best == 0: # if and only if we just reached a 0, and no predecessor
            # has even 1 left to move forward.
                return False

        return True
