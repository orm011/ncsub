class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # input[0][0] -> output[0][n - 1]
        # input[0][n - 1] -> output[n - 1][n - 1]
        # input[n - 1][n - 1] -> output[n - 1][0]
        # input[n - 1][0] -> output[0][0]
        # to do it in place, we need O(1) space to be enough. 
        # if we move lots of numbers, where do we store the ones in the destination.
        # idea: just follow the cycles above. each position  is in a cycle
        # with 4 other positions. 
        # [i][j] -> [j][n - i - 1] -> [n - i - 1][n - j - 1] ->  [n - j - 1][i] ->
        # [i][j] 
        # we should only loop through positions once. every position will
        # go through the top left quadrant once (i < n // 2, j < n // 2)
        # this should have exactly one member of each orbit
        # in the even case, 0..n//2 - 1 , n//2 ... n - 1 covers everything
        # in the odd case, n//2,n//2 itself is the middle element eg, 3//2 == 1. 1,1.
        # it will be skipped, so will remain fixed in place, as we need.
        # correction: row i = n//2 needs to move.

        half,rem = divmod(n,2)
        for i in range(half+rem):
            for j in range(half): # exclude top right bc that is accounted for by row i//2
                # copy lastval to make room for overwriting
                lastval = matrix[ n - j - 1] [i]
                pairs = [(i,j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]
                pairs = pairs[::-1] # reverse
                for (dst,src) in zip(pairs[:-1], pairs[1:]):
                    dsti,dstj = dst
                    srci,srcj = src
                    matrix[dsti][dstj] = matrix[srci][srcj]
                matrix[i][j] = lastval


