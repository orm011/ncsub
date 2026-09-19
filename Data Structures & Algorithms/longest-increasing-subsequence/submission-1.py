import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tricky aspect: there are many possible sequences.
        # some will start way later, and will look small vs old ones,
        # but eventually will become large.
        # some observations: one sequence contains many others,
        # so we only need to worry about maximal sequences.
        # consider a descening array: answer is 1. 
        # consider an ascending array: answer is n.
        # consider a v shaped sequence.
        # consider a ^ shaped sequennce.
        # consider ^v sequence. The solution could be the first or last
        # segment, we need to compare their lenghts
        # for a given sequence, we only need to track their last 
        # member and lengt, all future decisions only depend on those
        # 
        # consider a one pass algorithm, left to right.
        # 1, 4, 2, 3, 5
        # 1, 4, 5 is a sequence.
        # 1, 2, 3, 5 is better.
        # 
        # we choose 4 initially but may need to readjust with 2
        # 2 is better bc the length stays the same, but we know
        # no matter what comes after, will be at least as good as 4.
        # 
        # can I know at least the longest incr subsequence known so far.
        # imagine
        # .v pattern were the first dot will precede the bottom of the 
        # at position i, if we know the lowest possible end for a 
        # subsequence of size n (for each i) (may be null), then the next step,
        # can we construct the next solution with next value k.
        # for j in range(n):
        # if arr[j-1] < k < arr[j], we can update arr[j] = k.
        # note that arr[i] < arr[j] bc the lowest end for a 
        # sequence of length i must be lower than the j.
        
        n = len(nums)
        
        # first is sentinel
        best = [float('inf') for _ in range(n + 1)]
        best[0] = float('-inf')

        longest = 0
        for i,v in enumerate(nums):
            j = bisect.bisect_left(best, v)
            # for j in range(1,i+2):
            #     # to do. this should be binary search 
            #     if best[j-1] < v < best[j]: # will only match one location
            best[j] = v # this value should replace that sequence
            longest = max(longest, j) # update
                    #print(f"{best=} {longest=}")

        # runtime: O(n**2) due to nested loop.
        # 
        return longest


        



