class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # islands are 1's connected vertically or horizontally. transitive.
        # max area of island.
        # approach 1: frame it as graph problem, return size of largest connected
        # component. 
        # impl 1: traverse array, form graph by connecting cells previous or above, union find data structure tells us which component we are in.
        # impl 2: go through array, whenever we find a 1 we have not visited,
        # we do a dfs or bfs traversal of it, when done, we note the size.
        # we resume where we left off, skipping any already visited nodes.
        # time: O(m*n). 
        # space: O(m*n) for pending edges to check in DFS/BFS
        #  + O(m*n) for visited nodes so we dont check them again.

        stack = []
        # assume we can modify in place, otherwise copy.
        rows = m = len(grid)
        cols = n = len(grid[0])
        SEEN = -1
        maxsize = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: # skip previously seen
                    continue
                
                # == 1.
                stack.append((i,j))
                size = 0 # start empty.
                grid[i][j] = SEEN # do not traverse again

                while stack:
                    # get neighbors:
                    (cr,cc) = stack.pop()
                    # print(f"{(ii,jj)=}")
                    size += 1
                    # ok to mark as seen bc all neighbors will be added.
                    # they dont need to through node again 

                    # find neighbors
                    if cr > 0 and grid[cr - 1][cc] == 1:
                        grid[cr - 1][cc] = 0
                        stack.append((cr - 1, cc))

                    if cr + 1 < rows and grid[cr + 1][cc] == 1:
                        grid[cr + 1][cc] = 0
                        stack.append((cr + 1, cc))

                    if cc > 0 and grid[cr][cc - 1] == 1:
                        grid[cr][cc - 1] = 0
                        stack.append((cr, cc - 1))

                    if cc + 1 < cols and grid[cr][cc + 1] == 1:
                        grid[cr][cc + 1] = 0
                        stack.append((cr, cc + 1))
                
                maxsize = max(size, maxsize) # update


        return maxsize
                    

