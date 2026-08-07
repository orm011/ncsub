

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # want to remove entries equal to val, but pack the remaining
        # elements.
        # option 1: queue of positions.
        # add a position of deleted element to queue.
        # when a non deleted element is found, move it to the starting position.
        # and so on.
        # time O(n), space O(n) also bc of the queue. similar to just copying it to a
        # new array. we want to do in-place.
        # can we do it in space O(1)
        # keep pointer to first empty position.
        # and pointer current value. if we find a non-zero value, and the first empty 
        # position is set to something, we cna move it there.
        # then move the empty value pointer to the next cleared position. 
        # we can identify the cleared positions by their value being equal to val.
        cleared_pos = None
        for i, numval in enumerate(nums):
            if numval == val and cleared_pos is None:
                cleared_pos = i
            elif numval == val:
                continue
            elif numval != val and cleared_pos is not None:
                nums[cleared_pos] = numval # move to first cleared pos
                nums[i] = val # mark this as available
                while nums[cleared_pos] != val:
                    cleared_pos +=1 # will hit something for sure.
                continue
            else: # numval != val and cleared pos is None:
                continue # nothing to do here.
        
        # cleared pos already points to the first clear position
        return cleared_pos if cleared_pos is not None else len(nums)

        





        