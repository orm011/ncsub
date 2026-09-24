from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])

        LAND = 2**31 - 1
        WATER = -1
        CHEST = 0

        # shortest path between a chest and each 
        # land point in the graph defined by land
        # adjacency. Since each edge is size 1, 
        # BFS finds it.
        # start BFS with all treasures first,
        # so that we get the shortest distance from any 
        # treasure
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == CHEST:
                    queue.append((i,j,0))
                

        while queue:
            (i,j,dist) = queue.popleft()
            
            # sequencing.
            # check neighbors and add them to 
            # queue with increased distance,
            # as long as they have not been added 
            # to the queue. Equiv to theck == LAND,
            # and then we mark them.
            if 0 <= i - 1 and grid[i-1][j] == LAND:
                queue.append((i-1,j,dist+1))
                grid[i-1][j] = dist + 1 # final distance

            if 0 <= j - 1 and grid[i][j-1] == LAND:
                queue.append((i,j-1,dist+1))
                grid[i][j-1] = dist + 1 # final distance

            if i + 1 < m and grid[i+1][j] == LAND:
                queue.append((i+1,j,dist+1))
                grid[i+1][j] = dist + 1 # final distance

            if j + 1 < n and grid[i][j+1] == LAND:
                queue.append((i,j+1,dist+1))
                grid[i][j+1] = dist + 1 # final distance
            
            











        