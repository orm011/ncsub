import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # option 1: sort nums, iterate until have k distinct. 
        # Actualy wrong. its notk highest, its k highest *count*
        #
        # option 2: hash nums, keep count, then locate the highest k count. naive is iteration over collection, and sorting the counts.
        # option 3: use a heap on the counts, to get top k highest only.  # ie, heapify the counts.  This has k log (num differnt counts). 
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        counted = [(-count, num) for (num,count) in counts.items()]
        heapq.heapify(counted)
        ans = []

        while counted and len(ans) < k:
            (key, val) = heapq.heappop(counted)
            ans.append(val)

        return ans
        