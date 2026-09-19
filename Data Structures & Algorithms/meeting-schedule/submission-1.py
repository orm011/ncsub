"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # two (start_1, end_1), (start_2, end_2) are in conflict if and only if
        # they overlap. ie, wlog assuming start_1 <= start_2. conflict iff start_2 < end_1
        # from a given list of n intervals, how to find if there are any conflicting pairs.
        n = len(intervals)
        # assume sorted (by implicit key, start_i)
        intervals.sort(key=lambda x: x.start)

        prev_end = -float('inf')
        for interval in intervals:

            if interval.start < prev_end:
                return False
            prev_end = interval.end
            # this max may be unnecessary: if prev_end > end, then prev_end > start

        # time: O(n log n) sort step plus O(n) traversal
        # space: O(n ) sort (python is not quite in place)
        return True
        



