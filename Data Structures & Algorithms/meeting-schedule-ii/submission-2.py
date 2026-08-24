"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # guess: need as many meeting rooms as there 
        # are concurrent (overlapping) meetings
        # we know we need at least those, and once that is taken care of
        # the rest of time time is ok.
        # approach: if we sort by start time and keep jumping forward
        # in time, removing a meeting when it ends and opening another one when it starts (need a min heap to know the next end time). 
        
        # the max rooms needed is the max size of the heap
        heap = []
        # assume ok to mutate
        intervals.sort(key=lambda interval: interval.start)
        maxlen = 0
        for intr in intervals:
            while heap and heap[0] <= intr.start: 
                # end all intervals ending before this one start, 
                # as there is no overlap 
                heapq.heappop(heap)

            # heap[0] > intr.start 
            heapq.heappush(heap, intr.end)
            maxlen = max(maxlen, len(heap))
        
        return maxlen

        #analysis: 
        # O(n) space (sorting list)
        # O(n) space stack 
        # O(n) time
            



        