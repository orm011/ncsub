class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # input alrady sorted, disjoint intervals.
        # strategy: find insertion point.
        # then check for overlap with previous interval.
        # then check for overlap with as many next intervals as possible.
        # insertion point: O(n) or O(log n) using binary search.
        # end of overlap: search for interval end point on the ordered list of intervals
        # all the intervals in between are merged.
        # may need to remove O(n) intervals here.


        # old:   |----|        |-------|
        # new 1:             |------|
        # new 2:        |--|
        # new 3:                  |--------|
        # new 4: # not possible
        
        # phase 1: find first position
        current_end = None
        new_start, new_end = newInterval
        output = []

        for i, [start,end] in enumerate(intervals):
            if new_start > end:
                output.append([start,end])
            else: # new_start <= end:
                # we know no overlap with prev end.
                merged_start = min(start, new_start)
                current_end = max(end,new_end)
                if new_end < start:
                    output.append([new_start,new_end]) # case 2
                    output.append([start,end])
                elif current_end <= end:
                    output.append([merged_start,current_end]) # case 1
                else: # current_end > end. may stradle more segments # case 3
                    output.append([merged_start,current_end])
                break # 

        if current_end is None:
            output.append(newInterval)
            return output

        i+=1 # start next iter
        while i < len(intervals):
            [start_i,end_i] = intervals[i]
            if current_end >= start_i:
                output[-1][-1] = max(current_end, end_i)
            else:
                output.append([start_i, end_i])
            i+=1
        return output



        # new_start <= intervals[start_pos][1] # definitely overlaps
        # new_start > intervals[start_pos - 1][1] # or start pos is None # no overlap
        # new_end < intervals[end_pos][0] # no overlaps.
        # new_end >= intervals[end_pos - 1][0] definitely overlaps or end_pos is None
        

        


        


        