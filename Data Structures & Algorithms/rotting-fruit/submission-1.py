class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first impression:
        # non empty cells form a graph, edges based on vertical or horizontal
        # adjacency.
        # the connected components with a rotten fruit will eventually rot,
        # with time equal to minimum 
        # longest path from any of the rotten fruits
        # a connected component with only non-rotten will never rot.

        # strategy: 
        # we can do a graph search starting from every rotten fruit,
        # tracking the number of hops needed to reach each node.
        # tricky part #1: what matters is the shortest path, not the path
        # we used to get there
        # tricky part #2: there are multiple rotten fruits, so we need 
        # the shortest path to any rotten fruit.

        # shortest path algorithms based on one source applied one after the other may not be a good idea: repeated work.

        # lets think simpler:
        # we keep a list of rotten fruit.
        # we track time.
        # we iterate through the list and add new rotten spots.
        # only the newly rotten matter.
        # when there are no more newly rotten, it means we converged.
        # this number of iterations is important, this is the answer if there
        # are no spots left.
        # any left over spots are unreachable.
        # whats the cost of each iteration:
        # one pass to find all rotten positions, add to list.
        # for each, we add neighbors to next list.
        # total work: O(n*m) to get scan the full input.
        # + O(# fruits) queued work.

        counts = [0,0,0] # 0 1 and 2
        n = len(grid)
        m = len(grid[0])

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        pending = []
        for i in range(n):
            for j in range(m):
                counts[grid[i][j]] += 1
                if grid[i][j] == ROTTEN:
                    pending.append((i,j))
        

        # need to distinguish rounds to count distances
        current = []
        minutes = 0
        while pending:
            current = pending
            pending = []
            while current:
                (i,j) = current.pop()

                if 0 <= i - 1 and grid[i-1][j] == FRESH:
                    grid[i-1][j] = ROTTEN
                    counts[FRESH] -= 1
                    pending.append((i-1, j))
                
                if 0 <= j - 1 and grid[i][j - 1] == FRESH:
                    grid[i][j-1] = ROTTEN
                    counts[FRESH] -= 1
                    pending.append((i, j-1))
                
                if i + 1 < n and grid[i + 1][j] == FRESH:
                    grid[i+1][j] = ROTTEN
                    counts[FRESH] -= 1
                    pending.append((i+1, j))

                if j + 1 < m and grid[i][j + 1] == FRESH:
                    grid[i][j+1] = ROTTEN
                    counts[FRESH] -= 1
                    pending.append((i, j+1))

            if pending: # time only increases if there is more stuff to rot
                minutes += 1



        return -1 if counts[FRESH] > 0 else minutes
        