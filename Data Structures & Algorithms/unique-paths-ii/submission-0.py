class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # approach.
        # lets define numpaths[i][j] = # number of valid unique paths to this point from 0,0 
        # numpaths[0,0] = 1
        # numpaths[] is 0 for any cell with obstacles.
        # numpaths[i,j] could arrive from above, or from the left. so numpahts[i,j] = numpaths[i-1,j] + numpaths[i,j-1]
        # boundary case where j == 0 and or i == 0

        # initialize for obstacles.
        numpaths = [[-1 for val in obstacleGrid[0]] for _ in obstacleGrid]
        if m == 0 or n == 0:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    numpaths[i][j] = 0
                    continue
                
                if i == 0 and j == 0:
                    numpaths[0][0] = 1
                    continue

                # otherwise. 
                numpaths_from_above = numpaths[i-1][j] if i > 0 else 0
                numpaths_from_left = numpaths[i][j-1] if j > 0 else 0
                numpaths[i][j] = numpaths_from_above + numpaths_from_left

        return numpaths[-1][-1]