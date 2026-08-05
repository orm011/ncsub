class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # naive approach:
        # find original 0s, record positions,
        # for each position, change entries.
        # why: when we change entries to 0, how would we know which date 
        # from before any changes. the examples show we don't continue zeroing things.
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
        


        
        