import bisect
from collections import deque 
class LRUCache:

    def __init__(self, capacity: int):
        # need two pieces of state,
        # key value mapping
        # tracking who is LRU, and when they get evicted or used, who's new LRU

        # initial idea: a dictionary for key value mapping
        # tracking LRU feels tricky: does not stick to normal FIFO OR LIFO
        # things can go from anywhere in the ordering to the tail (MRU)
        # possible: 
        # python list/deque: both bad at removing things from the middle O(n) work.
        # python heap: time of use can be used as minheap, but modifying use time of existing element:
        # can always add it again with larger time of use,. getting min can be O(1), but old entries could
        # grow with length of history...
        # custom linked list: with pointers from keys: reordering elements to head is easy.
        # decision: list first.
        self.sorted_times = [] # (-time, key) in reverse ordering, smallest last
        self.value_map = {} # key -> (value, time)
        self.time = 0
        self.capacity = capacity

        ### problem: deque has no sort method... 
        ## list does, we could switch to list but we will have problems with popping the LRU 
        # unles we make the list be ordered in reverse. then LRU is easy to pop.

    def _update_sorted_times(self, oldtime, newtime, key):
        pos = bisect.bisect_left(self.sorted_times, (-oldtime,0))
        assert self.sorted_times[pos] == (-oldtime,key)
        self.sorted_times[pos] = (-self.time, key)
        self.sorted_times.sort()

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.value_map:
            ans,oldtime = self.value_map[key]
            # now update the time and update all data structures
            self.value_map[key] = (ans, self.time)
            self._update_sorted_times(oldtime, self.time, key)
            return ans
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.value_map: # existing entry, eviction not needed.
            (_, oldtime) = self.value_map[key]
            self.value_map[key] = (value, self.time)
            # find current record
            # since time is unique for each record, and record must be there, pos 
            # will be the exact location
            self._update_sorted_times(oldtime, self.time, key)
        elif len(self.value_map) < self.capacity: # ok to just add
            self.value_map[key] = (value, self.time)
            self.sorted_times.append((-self.time, key))
            self.sorted_times.sort()
        else: # at capacity, first evict.
            (_, lrukey) = self.sorted_times.pop() # rightmost is LRU
            del self.value_map[lrukey]            
            
            # now add new value
            self.value_map[key] = (value, self.time)
            self.sorted_times.append((-self.time, key))
            self.sorted_times.sort()
        
