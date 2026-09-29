class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## O(1) space: only one or two memories.
        # keep track of first and second top counts. 
        # drop anything that falls below second.
        # hypothesis: if an element shows up n/2 or more, 
        # then it will rise to the top, even if we don't track it.
        # problem: how do numbers enter the counter
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1


            
        return candidate
        