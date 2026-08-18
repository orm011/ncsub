import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we replace 2 heaviest y >= x with 
        # one y - x one (unless 0) eventually we get down 
        # to either a lone small number left (if the other two are gone before)
        # or otherwise, 0 iff last two are identical.
        # invariants:
        # reduce number of stones by 1 or 2 per round.
        # we cannot know which will be the next round...
        # at every step get the two top stones, check what will replace them.
        # can be done with a heap
        heapq.heapify_max(stones)
        while stones:
            if len(stones) == 1:
                return stones[0]
            top1 = heapq.heappop_max(stones)
            top2 = stones[0]
            diff = top1 - top2 
            if diff > 0:
                heapq.heapreplace_max(stones, diff)
            else:
                heapq.heappop_max(stones)


        return 0
        