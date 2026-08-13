import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # naive exhaustive apporach:
        # compute max at every window. : O(n k)
        # better approach: max  of a changing set can be tracked
        # using a max-heap, making each window slide update log k, 
        # need to add new number, remove old one.
        # O( n log k)
        num_heap = list(zip(nums[:k-1], range(k-1)))
        heapq.heapify_max(num_heap)
        # store pairs (val, pos)
        ans = []
        for idx in range(k - 1, len(nums)):
            # add new elt
            heapq.heappush_max(num_heap, (nums[idx], idx))
            while num_heap and num_heap[0][1] <= idx - k: 
                # bounds check: when idx is k - 1, bound is < 0.
                heapq.heappop_max(num_heap)
            
            # this max is within bounds
            ans.append(num_heap[0][0])
            # print(f"after {idx=} {num_heap=}")


        # runtime: O(n log n)
        # space: O(n)
        # depending on the ordering, if max numbers are sorted desc,
        # then it is O(n log k) (will always pop) and O(k) space.
        # if numbers are sorted asc: will grow to O(n log n)
        return ans

        