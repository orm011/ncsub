import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # without sorting:
        # can track the k largest seen so far.
        # whenever a new number exceeds the kth largest, we 
        # remove the old kth largest and re-arrange. 
        # this is O(n log k) if we do it with a heap: 
        # the heap is a min-heap  with the k largest elements.
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
                continue
            elif n <= heap[0]: # already got k, but nothing to do
                continue
            else:
                heapq.heapreplace(heap, n)
            
        return heap[0]


