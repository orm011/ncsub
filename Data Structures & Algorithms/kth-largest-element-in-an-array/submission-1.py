class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums are very limited in size, note -1k to 1k.
        counts = [0 for _ in range(-1000,1001)]
        for n in nums:
            counts[n+1000] += 1
        
        for i in range(2000, -1, -1):
            k -= counts[i]
            if k <= 0:
                return  i - 1000

        