import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # option one sort: every time we update will be expensive.
        # option 2: heap, but heap only gives directly largest.
        # Also note: we only add entries.
        # if we keep track of the k largest so far,
        # when we get a new element, it either falls below the k largest so far
        # so it does not matter
        # or it is bigger than the kth largest, in which case the 
        # new largest is from the set of k-1 largest and that new element.
        # since we only add elements, we do not need to worry about 
        # having to go back to previous.
        # time: O(n) construction (n = len(nums))
        # O(log k) during add (if new is larger)
        # space: O(k) after initial construction
        
        self.topk = nums
        heapq.heapify(nums)
        self.k = k
        while len(self.topk) > k:
            heapq.heappop(self.topk)
        
    def add(self, val: int) -> int:
        if len(self.topk) == self.k:
            curr = self.topk[0]
            if val <= curr:
                return curr
            
            # val > curr, curr will pop
            heapq.heapreplace(self.topk, val)
            return self.topk[0]
        else:
            heapq.heappush(self.topk, val)
            return self.topk[0]


        
