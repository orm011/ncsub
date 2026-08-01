class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # every number appears twice, except one.
        # to do this in one pass, lets build a hash as we go.
        seen = set({})
        for n in nums:
            if n not in seen: # firs time, track
                seen.add(n)
            else: # second time, remove as possibility
                seen.remove(n)

        return next(iter(seen))

        