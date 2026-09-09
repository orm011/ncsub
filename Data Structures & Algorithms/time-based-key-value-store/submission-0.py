from sortedcontainers import SortedList
from collections import defaultdict
import bisect

# timestamps are strictly increasing

class TimeMap:

    def __init__(self):
        self.key2vals = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # assumption: set() order timestamps are increasing 
        self.key2vals[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.key2vals[key]
        if arr == []:
            return ""
        
        # pos > len(arr) or arr[pos] > timestamp 
        pos = bisect.bisect_right(arr, timestamp, key=lambda p: p[0])

        if pos == 0:
            return "" # too early
        else:
            return arr[pos - 1][1]
        

# for each key, there is a timeline of values, 
# instead of a single one.
# option : use a map of keys => (value array, timearray), or some structure like that. 
# set adds the value and time. note there are many timestamps.
# so we need to design for that, and many calls.


# problem with array: it is not easy to keep entries sorted
# without incurring O(N) overhead each time we insert.
# we need to be able to find, for a given get timestamp, the 
# predecessor in the list. 

