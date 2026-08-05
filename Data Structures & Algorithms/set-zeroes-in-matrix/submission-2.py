class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # naive approach:
        # find original 0s, record positions,
        # for each position, change entries.
        # why: when we change entries to 0, how would we know which date 
        # from before any changes. the examples show we don't continue zeroing things.

        # space: O(n)
        # time: O(n*m) (scanning the initial matrix)
        # we know best possible time scenario is O(n * m)
        # can we get space to be lower?
        # we need to process work item (Row i col j) as soon as we encounter it, 
        # but we dont want to mistake any of the points in col i or row j as work items.
        
        # when we proces (i, j), we can stop iterating through that row?
            # actually no, some entries may imply work which would be missed.
            # what if i, j + 1 was also 0, then we can forget about row i, but not about col j+1, and there could be multiple j+2... to remember. 
            # we could immediately start procesing col j+1. 
            # any zeros above row i are not important.
            # but zeros below it, 

        # random idea: what if we traverse the matrix diagonally in some way. 
        # 0,0, 1,0, 0,1 , 0,2, 1,1, 2,0,3,0
        # when we find a 0, we zero out everything to the left and above it. This means
        # we are not zeroing out anything that we have not processed yet.
        # but how do we ensure we zero out evertying to the right and below?
        # as we traverse, we check above and to the left.
        # seems to break in some cases.

        # note if a row has 
        # alternative idea: current problems are caused by lack of an easy way to tell
        # whether a 0 is original or propagated. 
        # we attempted using execution ordering somehow to guess, this but it doesnt quite work


        # python lists hand handle more than just integer values however, 
        # we so can use a separate out of domain symbol to mark things up. for flipping
        # in one pass.
        # then in a separate pass we only flip those.
        # this solution is very language/domain dependent, not worth exploring.

        # note constraints: matrix is not that big. hence even O(matrix ) is O(1)...
        # lets assume by O(1) we mean a structure that does not depend in size on the 
        # size of the matrix.


        
        rows = set()
        cols = set()

        # we only need the rows and columns, not the entries.
        # O(n+m) space instead O(mn) in worst case
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = matrix[i][j]
                if val == 0:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0

