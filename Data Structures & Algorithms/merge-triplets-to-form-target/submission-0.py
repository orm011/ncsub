class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # is there a subset of triplets such that 
        # target1 = max(target1_i)
        # target2 = max(target2_i)
        # target3 = max(target3_i)

        # easy cases where not possible.
        # min(target_2i) for all the tuples where target3  matches is 
        # greater than.

        # for each dimension of the target value (0,1,2)
        # find all tuples with value less than or equal to the target
        # their intersection is a solution (still need at least one equal
        # for each dimension)

        n = len(triplets)
        ta, tb, tc = target
        ba, bb, bc = (float("-inf"), float("-inf"), float("-inf"))
        for (a,b,c) in triplets:
            if a <= ta and b <= tb and c <= tc: 
                # cannot use anything larger
                ba, bb, bc = max(ba, a), max(bb, b), max(bc, c)

        return [ba, bb, bc] == target
        # runtime: O(n)

        


        