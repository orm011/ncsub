class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        # brute force: try every pair of positions, pick best.
        # O(n**2)

        # other ideas
        # For a fixed left l position, whats the best right position.
        # (optimal solution will have the optimal right position for 
        # its left position, which we dont know yet)
        # We know some ending positions are better than others.
        # ie any position i beats any j < i such that height[j] <= height[i]
        # We also know that height[l] bounds the effect of larger ...
        
        # other ideas:
        # start with fully to the left and right (two pointers)
        # the binding constraint is the smaller height, assume wlog left.
        # move the left one to the first better position to start if any.
        # (if nothing then keep it)

        # why would this be optimal?
        # consider an optimal solution.
        # it cannot be improved further by moving its smaller side left or right any distance.

        # if we hit one side of that solution, the smaller side will fall into place.
        # so the question is will we hit the other side.
        # the optimal will need to be 

        left = 0 
        right = len(heights) - 1

        def water(i, j):
            height = min(heights[i], heights[j])
            width = j - i
            return height * width

        best = water(left, right)
        
        while left < right:
            contents = water(left, right)
            best = max(best, contents)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return best