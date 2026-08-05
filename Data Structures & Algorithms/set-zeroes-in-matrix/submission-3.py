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
        
        # lets just store None in the positions (bc our data structure allows this)

        # we only need the rows and columns, not the entries.
        # O(n+m) space instead O(mn) in worst case
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for c in range(len(matrix[i])):
                        if matrix[i][c] != 0: # do not erase any original 0s.
                            matrix[i][c] = None

                    for r in range(len(matrix)):
                        if matrix[r][j] != 0:
                            matrix[r][j] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0



