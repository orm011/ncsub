import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we care to find the path  min_p max_cell h. that number is the time it would take.
        # shortest path is normally expressed as minimizing min_p sum_cell. 
        # approach: we can use a shortest path algorithm where instead of sum we use max.
        # at every point, we expand using the minimum, total outgoing. eventually we will hit the corner and we stop
        
        ## correction: the weights here are assigned to vertices.
        ## can we still use a similar reasoning

        ## eg [[7]] it takes 0 time to reach this.
        ## [[7], [1]] it takes time 7 to reach
        # [[7], [8]] takes 8 time to reach


        vertices = sum([[(i,j) for i in range (len(grid))] for j in range(len(grid))], [])

        def get_neighbors(node):
            (i,j) = node
            horizontal = [(h,k) for (h,k) in [(i,j-1), (i, j+1)] if k >= 0 and k < len(grid)]
            vertical = [(h,k) for (h,k) in [(i+1, j), (i-1, j)] if h >= 0 and h < len(grid)]
            return horizontal + vertical
        
        best_paths = {(0,0):grid[0][0]}
        next_move = [] # (max_to_hk from (i,j), (i,j) , (h,k))


        # act like djikstra.
        # we have a set that includes the minium time for each included node to be reachable for (0,0)
        # at each step, there are new nodes that can be added with the minimum time to get to any given node
        #  is max(opt_previous_node, node_val)
        last_added = (0,0)
        while True:
            found_next = False
            neighbors = get_neighbors(last_added)

            for (i,j) in neighbors:
                path_height = max(best_paths[last_added], grid[i][j])
                heapq.heappush(next_move, (path_height, (i,j)))

            while True:
                next_path_height, next_vertex = heapq.heappop(next_move)
                if next_vertex not in best_paths:
                    found_next = True
                    break
            
            if found_next and next_vertex == (len(grid)-1, len(grid)-1):
                return next_path_height
            elif found_next:
                best_paths[next_vertex] = next_path_height
                last_added = next_vertex
            else:
                assert False


                




        





        