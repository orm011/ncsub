import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        # alternative: quickselect.
        # eg median: pick a number at random. count numbers before and after.
        # that gives you the position of the number.
        # now on the set that would contain the median.
        # pick a number at random, new rank. 
        # now onto set that contains median.
        n = len(nums)
        pivotpos = None
        start = 0
        end = n - 1
        while pivotpos != k - 1:
            pos = random.randrange(start, end+1)
            pivot = nums[pos]
            ptr1 = start
            ptr2 = end

            # invariant: 
            # ptr1 is 0 or all nums[:ptr1] > pivot
            # ptr2 is n - 1 or all nums[ptr2:] <= pivot  
            while ptr1 < ptr2:
                if nums[ptr1] > pivot >= nums[ptr2]:
                    ptr1 += 1
                    ptr2 -= 1
                elif nums[ptr2] > pivot  >= nums[ptr1]:
                    nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                    ptr1 += 1
                    ptr2 -= 1
                elif nums[ptr2] > pivot:
                    ptr1 += 1
                    # ptr2 stays
                else: # nums[ptr1] <= pivot
                    ptr2 -= 1
                
            # ptr1 == ptr2 or ptr2 < ptr1 if they crossed over.
            if ptr1 == ptr2: # only one moved.
                if nums[ptr1] > pivot:
                    pivotpos = ptr1 + 1
                else:
                    pivotpos = ptr1

            if ptr2 < ptr1:
                pivotpos = ptr1

            i = pivotpos            
            while True:
                if nums[i] == pivot: #swap
                    nums[i], nums[pivotpos] = nums[pivotpos], nums[i]
                    break
                else:
                    i+=1
            
            #assert nums[pivotpos] > pivot
            if pivotpos > k - 1: # exceeds # will reduce at least by 1.
                start = start
                end = pivotpos
            elif pivotpos < k - 1 and pivotpos > start: # what if we picked the smallest elt.
                start = pivotpos
                end = end
            elif pivotpos == start:
                start += 1 # move forward
                end = end
            else:
                return nums[pivotpos]

            # print(f"{pivot=} {nums=} {pivotpos=} {start=} {end=}")

            # for num in nums[:pivotpos]:
            #     assert num > pivot
            # for num in nums[pivotpos:]:
            #     assert num <= pivot            


        return nums[pivotpos]



            

             



