class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # can deduce missing num from sum total
        n = len(nums)
        total = (n*(n+1)) // 2
        return total - sum(nums)
        
    # for 1 number: sum is : 1*(2)//2 = 1.
    # total will work.
    
    # space O(1) 
    # sum loop is O(n) time