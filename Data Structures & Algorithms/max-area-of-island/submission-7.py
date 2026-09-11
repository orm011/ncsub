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
        m = len(grid)
        n = len(grid[0])
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
                    (ii,jj) = stack.pop()
                    # print(f"{(ii,jj)=}")
                    size += 1
                    maxsize = max(size, maxsize) # update
                    # ok to mark as seen bc all neighbors will be added.
                    # they dont need to through node again 

                    # find neighbors
                    posns =[[ii-1,jj], [ii+1,jj], [ii,jj-1], [ii,jj+1]]
                    for [h,k] in posns:
                        if not 0 <= h < m:
                            continue
                        if not 0 <= k < n:
                            continue
                        if grid[h][k] != 1: # either seen or 0
                            continue
                        # found neighbor in island:
                        stack.append((h,k))
                        grid[h][k] = SEEN # do not add again


        return maxsize
                    

