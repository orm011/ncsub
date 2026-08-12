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
        solutions = set()
        current = []
        def build_solns(*, r: int, target: int, index: int) -> None: 
            # r remaining levels. 
            # index: allowed lowest index
            nonlocal current

            if r == 1 and index < len(nums) and target >= nums[index] and target in numset:
                current.append(target)
                solutions.add(tuple(current))
                current.pop()
            elif r >= 2:
                for i in range(index, len(nums)): 
                    # only explore indices beyond current
                    k = nums[i]
                    current.append(k)
                    build_solns(r=r - 1, target=target - k, index=i + 1)
                    current.pop()

        build_solns(r=3, target=0, index=0)
        # ensured no duplicate indices but not globally unique solutions.
        # now, we have gone the other way. too aggressive.
        # we do allow repeated values, as long as there are multiple copies.
        # now we do allow repeated values, but are running into dups again.
        # easy solution: just remove dupes using a solution set.
        return list(solutions)



        