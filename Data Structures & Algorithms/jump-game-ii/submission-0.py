class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy left to right would not work, bc we may get stuck later on.
        # think backward from last position, which could be the last jumps to it
        # then back again

        # going right to left: we can start last and move back, some 
        # positions clearly cannot reach the last position. for those who can,
        # we can also track who can reach those or the last.
        # note: if we can assume there is always a valid answer to get to the last one,then there is always a valid answer to get to any position (bc we had to go 
        # through them to get to the last).
        # hence, if we go right to left, we are always better off picking the 
        # the longest jump that reaches the end (the earliest one).
        # but then we also want to track the earliest position that reaches the
        # best second-last: 
        # the current best launch pad: k
        # we keep going, if we find h such that h + nums[h] >= k great, keep it.
        # but if it also is h + nums[h] >= n - 1, keep it but remove k, no longer needed
        n = len(nums)
        stack = [n-1]
        for i in range(n-2, -1, -1):
            last = None
            while stack and i + nums[i] >= stack[-1]:
                last = stack.pop()
            
            if last: # restore last one
                stack.append(last)
                stack.append(i) # jumps to last
            else:
                # this position did not get us to 
                # last
                continue 

        return len(stack) - 1 # n - 1 does not count

        
        