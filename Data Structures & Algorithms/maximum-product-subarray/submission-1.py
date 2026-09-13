class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # note: they include negative numbers, and 0.
        # since two negatives cancel each other, adds a twist.
        # nums are all small. and product will not overflow.

        # subarray is parametrized by two pointers
        # adding a product may cause a negative, but the 
        # current subarray may still be part of optimal bc of 
        # later negatives. 

        # a zero means you can compare 0 products to either side
        # simplifies problem to some extent, to three options: left side, right side or 0 (multiple equivalent solutions)

        # any positive or 1 is neutral, always just expand.
        # as we try options. probably want to track: best product seen so far.
        # largest positive product so far
        # "largest" negative product so far, could turn sign.
        # have seen any 0 (escape hatch)

        # two pointers. expand end? or start at end and decrease?
        # ituition: lets start small, eg any 0 anywhere will make
        # everything 0, so no signal when moving pointers.

        best = nums[0]
        maxprod = nums[0]
        minprod = nums[0]

        j = 0 # j is pointer to last element included.
        n = len(nums)

        for j in range(1,n):
#            print(f"{j=} {best=} {maxprod=} {minprod=}")
            elt = nums[j]
            if elt >= 0:
                maxprod, minprod = max(maxprod*elt, elt), min(minprod*elt, elt)
            elif elt < 0:
                maxprod, minprod = max(minprod*elt, elt), min(maxprod*elt, elt)

            best = max(best, maxprod)


        return best










        