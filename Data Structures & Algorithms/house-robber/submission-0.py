class Solution:
    def rob(self, nums: List[int]) -> int:
        # base cases: empty list: value 0
        # single number: value of element.
        # recursive reasoning:
        # at point n, to decide whether to rob house n, 
        # we want to look at whats the best we can do if we instead rob house n-1,
        # vs robbing house n and then optimal robbing from house n-2
        # rob(n) = max (rob(n-1), nums[n] + rob(n-2))
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            pass

        robn = [-1 for _ in range(len(nums)+1)]
        robn[0] = 0
        robn[1] = nums[0]
        for i in range(2,len(nums)+1):
            robn[i] = max(robn[i-1], nums[i-1] + robn[i-2]) # nums array starts at elt 1.
        return robn[-1]
