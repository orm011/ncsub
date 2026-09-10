import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # each point has a distance to origin. norm.
        def normsq(v):
            x,y = v
            return x**2 + y**2

        n = len(points)
        # we need to scan points, and pick the min k.
        # we can sort
        # or we can use a min heap.
        # we can then heapify them in O(n)
        # and we get the top k in n + k log n in time.
        if n <= k:
            return points
        
        pts = [(normsq(p), p) for p in points]
        heapq.heapify(pts)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pts)[1])

        return ans