import bisect 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # consider sorting by ending time.
        # when considering solutions including k+1,
        # all of the previous intervals end before k+1 does,
        # which intervals overlap with the start of k+1?
        # if interval j overlaps with it. endinj > startk+1
        # then internval j+1, which ends after endinj, also must satisfy this constraint.
        # hence the remaining problem is a prefix of this problem.
        # if k+1 not included, only need to know about solution for k. 
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        optimal = [1 for _ in intervals]
        n = len(intervals)
        # optimal[i] = # max number of  non overlapping intervals in set [:i+1]
        # answer is n - optimal[n-1]
        
        # in reverse order, starting from 0
        # # endj > starti.
        # can we quickly solve: i -> prefix i.
        # option 1: binary search using already sorted endj. 
        # note starti may have no pattern,  can be way back or not.


        for i in range(1,n):
            # optimal w/o ith:
            woi = optimal[i-1]
            [starti, _] = intervals[i]

            #subprob = -1
            # this loop makes the overall loop potentially quadratic.
            # we know we can answer this query easily, by separately building
            # the graph from before.
            subprob = bisect.bisect_right(intervals, starti, lo=0, hi=i, key=lambda x: x[1])
            #for j in range(i - 1, -1, -1):
                # (_, endj) = intervals[j]
                # if endj <= starti:
                #     subprob = j
                #     break

            with_i = 1 + optimal[subprob - 1] if subprob > 0 else 1
            optimal[i] = max(with_i, optimal[i-1])
            #print(f"{optimal=}")

        return n - optimal[n-1]