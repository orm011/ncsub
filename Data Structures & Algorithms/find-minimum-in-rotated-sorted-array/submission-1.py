class Solution:
    def findMin(self, nums: List[int]) -> int:
        # numbers are sorted + rotated.
        # not consecutive.
        # return minimum.
        # challenge we dont know the rotation (knowing rotation is qual to knowiing min)
        # there are only n = len(nums) possible rotations
        # we are searching for some test that reduces possibilities by half.
        # consider the middle element.
        # we can compare to first
        # if array is rotated k < n//2, the top k element start the work, and then resets.
        # this happens if and only if nums[0] > nums[n//2].
        # 
        # Bc the max element is before nums//2, and all 
        # elements after will be smaller than nums[0].
        # if nums[0] > nums[n//2] then rotation must be between them inclusive.
        # otherwise it is on n//2 + 1 : 
        # lets say rotation r is the position of the smallest element.
        n = len(nums) 
        start = 0
        end = n - 1 # end is valid.
        i = 0
        while end - start > 0:
            mid = start + ((end - start)>>1) # can be == start. never eq end.

            # if i < 6:
            #     print (f"{start=} {end=} {mid=} {end - start=}")
            #     i +=1 
            # else:
            #     break
            
            # when end = start + 1.
            # mid == start.
            # so first check is false.
            # second could be true. breaks next time.
            if nums[start] > nums[mid]:
                start = start + 1 # start cannot possibly be answer, ensure progress.
                end = mid # include current mid which could be the answer
            elif nums[mid] > nums[end]: # (cannot be eq by constraint)
                start = mid + 1
                # end stays constant
            else: # its all ordered. 
                break
        # end[i] - start[i] decreaeses. if end - start == 2, mid is start + 1.
        # end  is mid + 1 = prevous end (not good)

        # consider only one left: end = start + 1. 
        # thats the answer.
        # consider two left: start, start + 1, start + 2.
        # mid = start + 1. 
        # if start is larger, move start by 1, include mid => next next time.
        # if start is smaller (eg no rotation).
        # conswider three left:  

        return nums[start]
