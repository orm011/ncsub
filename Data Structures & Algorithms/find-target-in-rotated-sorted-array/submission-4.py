class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial solution 1: find the rotation offset.
        # then do binary search with offset indices where 0 -> offset.
        # k -> (k + offset) % len(nums)
        # the rotation offset takes O(n)
        # getting to log(n) time: 
        # option 1: get to offset via some other kind of log n search. 
        ## finding a jump:
        ## imagine offset = k (!= 0)
        ## then arr[0] >= arr[len]
        ## but arr[k] <= arr[len]
        ## arr[k-1] > arr[k] # elts are unique (not eq)
        
        # idea: while arr[left] > arr[right]
        # part 1: find offset
        left = 0
        right = len(nums) - 1
        
        # if nums[left] > nums[right] and left + 1 == right,
        # then right is the offset.
        if nums[0] < nums[right]:
            offset = 0
        else:
            # precondition here is that there is an offset.
            while left + 1 < right:
                mid = left + (right - left) // 2
                # if right > left + 2  then 
                # mid >= left + 1
                # hence, either left will move
                # or right will move
                if nums[left] > nums[mid]:
                    right = mid
                else: # nums[left] <= nums[mid] hence > nums[right]
                    left = mid
            
            offset = right

        #print(f"pre {left=} {mid=} {right=}")
        #print(f"{offset=}")
        # offset good now.
        # now do binary search
        left = 0 
        right = len(nums) - 1
        n = len(nums)
        # idea: do a normal binary search, but access the array accouting for the offset.
        # nums = [nums[(i + offset) % n] for i in range(len(nums))]
        # print(f"{nums=}")
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     print(f"{left=} {mid=} {right=}")
        #     if target == nums[mid]:
        #         return mid
        #     if target > nums[mid]:
        #         left = mid + 1
        #     else: # target < nums[mid]
        #         right = mid - 1
        while left <= right:
            mid = left + (right - left) // 2
            #print(f"pre {left=} {mid=} {right=}")
            offset_mid = (mid + offset) % n
            if target == nums[offset_mid]:
                return offset_mid
            if target > nums[offset_mid]:
                left = mid + 1
            else: # target < nums[mid]
                right = mid - 1
            
            #print(f"post {left=} {mid=} {right=}")

            
        return -1