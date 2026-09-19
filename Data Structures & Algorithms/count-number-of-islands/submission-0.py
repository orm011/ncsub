class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of islands: number of connected components in graph.
        # edges are defined by vertical or horizontal adjacency.

        # max 100x100 size grid (10**4 vertices). 

        # we can do a graph traversal every time we reach a one. 
        # we want to make sure to avoid visting nodes we already visited
        # during traversal to not do duplicate work.

        
        # boolean array to track visits, could mutate input but rather not.

        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in grid[0]] for _ in grid]
        work = []
        def traverse(node: tuple[int, int]) -> None:            
            work.append(node)

            while work:
                (i,j) = work.pop()
                # add all '1' nodes we have not visited or scheduled to visit
                if 0 <= i-1 and grid[i-1][j] == '1' and not visited[i-1][j]: 
                    visited[i-1][j] = True
                    work.append((i - 1, j))
                if 0 <= j-1 and grid[i][j-1] == '1' and not visited[i][j-1]:
                    visited[i][j -1 ] = True
                    work.append((i, j - 1))
                if i + 1 < m and grid[i+1][j] == '1' and not visited[i+1][j]:
                    visited[i+1][j] = True
                    work.append((i + 1, j))
                if j + 1 < n and grid[i][j+1] == '1' and not visited[i][j+1]: 
                    visited[i][j+1] = True
                    work.append((i, j+1))
                 
        total_components = 0
        for i in range(m):
            for j in range(n):
                match grid[i][j], visited[i][j]:
                    case '0', _:
                        continue
                    case '1', True:
                        continue
                    case '1', False:
                        total_components += 1
                        traverse((i,j))
                    case _:
                        assert False, "unknown case"
            
        return total_components




        