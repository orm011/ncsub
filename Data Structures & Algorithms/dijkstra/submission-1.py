import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # key idea: like BFS, grow the set of shortest paths of A, by always picking the shortest (min depth) total distance
        # next step. by definition, that will be the shortest path to that node
        # ends when no edge is left that expands the boundary.
        edge_heap = []
        edge_map = { i:[(u,v,w) for (u,v,w) in edges if u == i] for i in range(n)}


        shortest_paths = {i:-1 for i in range(n)}
        shortest_paths[src] = 0
        new_vertex = src
        change = True
        while change: # we stop when no new vertex is added in the previous iteration.
            change = False
            # extend new boundary edges weighted by total path to n
            for (u,v,w) in edge_map[new_vertex]:
                heapq.heappush(edge_heap, (w + shortest_paths[u], u, v))

            while edge_heap != []:
                (next_w, _, maybe_next_v) = heapq.heappop(edge_heap)
                if shortest_paths[maybe_next_v] == -1:
                    new_vertex = maybe_next_v
                    shortest_paths[new_vertex] = next_w
                    change = True
                    break
            
        return shortest_paths

        




        
        

