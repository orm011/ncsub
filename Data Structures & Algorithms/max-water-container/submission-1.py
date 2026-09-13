from collections import deque

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # lets start with solution = [0,n]
        n = len(heights)
        start = 0
        end = n - 1

        def water(start,end):
            h = min(heights[start],heights[end])
            w = end - start
            return h*w


        l2r = deque([0])
        r2l = deque([n-1])
        for i in range(n):
            if heights[i] > heights[l2r[-1]]:
                l2r.append(i)
            
        for i in range(n-1,-1,-1):
            if heights[i] > heights[r2l[-1]]:
                r2l.append(i)

        # intuition:
        # move the lower end, check how it does by moving to the right. 
        # once it stops being the lower end.
        # stop moving it. 
        best = water(0, n-1)
        while l2r and r2l and (len(l2r) + len(r2l) > 2) and l2r[0] < r2l[0]: 
            while len(l2r) > 1 and heights[l2r[0]] < heights[r2l[0]]:
                l2r.popleft() # discard
                best = max(best, water(l2r[0], r2l[0]))

            while len(r2l) > 1 and heights[l2r[0]] >= heights[r2l[0]]:
                r2l.popleft()
                best = max(best, water(l2r[0], r2l[0]))
            
        return best









        




