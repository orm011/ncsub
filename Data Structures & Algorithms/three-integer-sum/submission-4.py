from collections import Counter

class Solution:
    # one approach:
    # triple nested loop checking sums of non equal indices.
    # a set of existing results to dedup
    # runtime O(n^3)
    # space for results could be also O(n^3) in general.
    # alternative: two levels of recursion. and match 
    # the third number exactly: O(n^2)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # cannot re-use an index AND multiple index combinations
        # could result in a duplicate if the values are repeated
        nums.sort() # in place sorting.
        numset = set(nums)
        solutions = []
        current = []
        def build_solns(*, r: int, target: int, index: int) -> None: 
            # r remaining levels. 
            # index: allowed lowest index
            nonlocal current
            if index >= len(nums) or target < nums[index]:
                return 

            if r == 1 and target in numset:
                current.append(target)
                solutions.append(current.copy())
                current.pop()
            elif r >= 2:
                i = index
                while i < len(nums): 
                    # only explore indices beyond current
                    k = nums[i]
                    current.append(k)
                    build_solns(r=r - 1, target=target - k, index=i + 1)
                    # can repeat value within same solution
                    # but need to skip forward to next unique value after using it.
                    current.pop()
                    while i < len(nums) and nums[i] == k:
                        i+=1 # skip forward to next possible value

        build_solns(r=3, target=0, index=0)
        # ensured no duplicate indices but not globally unique solutions.
        # now, we have gone the other way. too aggressive.
        # we do allow repeated values, as long as there are multiple copies.
        # now we do allow repeated values, but are running into dups again.
        # easy solution: just remove dupes using a solution set.
        # better solution: skip ahead on the loop. 

        # total complexity: O(nlogn) + O(n) + O(n^2) (we really remove half the space though). 
        # total space: O(n^2) for the solution set.

        return solutions

        # how things went here:
        # first i excluded too many tuples, ie, tuples with the repeated values.
        # (using unique keys)
        # then i included repeated tuples. (same values coming from different positions)
        # then i solved that in a quick and dirty way
        # then a fixed that.
        # a lot of trial and error here, ie i rely on the test suite to tell me how im doing




        