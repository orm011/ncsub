from collections import deque

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

        # assume we can modify in place, otherwise copy.
        m = len(grid)
        n = len(grid[0])
        SEEN = -1
        maxsize = 0

        queue = deque([(0,0)])
        currsize = 0 #grid[0][0] # current component size (1 or 0)
        grid[0][0] |= 2 # bit for added to stack
        while queue:
            #print(f"{queue=} {currsize=} {maxsize=}")

            # get node
            ent = queue.pop()
            if ent is None:  # marker added when found a new component, end reached.
                currsize = 0
                continue
            
            (ii,jj) = ent

            if grid[ii][jj] & 0b1 == 0: # not a 1.
                currsize = 0 # we have finished one component.
            else: # starting a new component
                if currsize == 0:
                    queue.append(None) # marker
               # print(f"{(ii,jj)=}")
                currsize += 1
                maxsize = max(currsize, maxsize)

            # find neighbors
            posns =[[ii-1,jj], [ii+1,jj], [ii,jj-1], [ii,jj+1]]
            for [h,k] in posns:
                if not 0 <= h < m or not 0 <= k < n:
                    continue
                if grid[h][k] & 0b10: # already added and counted
                    continue

                if grid[h][k]: # 1
                    queue.append((h,k)) 
                else: # == 0
                    queue.appendleft((h,k)) # delay processing.
                
                grid[h][k] |= 2 # added to stack


        return maxsize

        # remaining issue: how to delimit components in the queue.        
        # analysis: each node is only added to the stack at most once.
        # time O(m*n)
        # space: O(m*n) if we keep adding to the stack


                    

