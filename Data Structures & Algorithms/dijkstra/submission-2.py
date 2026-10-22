import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # dijkstra high level:
        # fixed source s.
        # d*[u] is shortest path from s to u (say infinite if no path)
        # optimality condition (general)
        # shortest distance to u is based on picking
        # an optimal path to a predecessor, and then having its
        # total be the smallest over all.
        # d*[u] = min_v in graph (d*[v] + w(v,u)) 

        # dijstra creates an ordering.
        # d*[s] = 0 # base case (unless there were negative cycles)
        # insight 
        # min_x neighbor of x d*[s] + w(s,x) := d'[x] = d*[x]
        # bc. min_v in graph (d*[v] + w(v,x)) will have 
        # d*[v] >=  d'[x] hence d'[x] >= d*[x] and d[x] <= d*[x]

        settled = [-1 for _ in range(n)] # d*[i] known.
        heap = [(0, src)] # initialize with total distance
        outgoing = defaultdict(list) # directed edges, outgoing
        for [u,v,w] in edges:
            outgoing[u].append((v,w))

        while heap:
            (dist, nodeid) = heapq.heappop(heap)
            if settled[nodeid] >= 0:
                # already expanded it once
                # and already optimal 
                continue  

            # mark it settled, this is the best distance
            settled[nodeid] = dist
            for dest, w in outgoing[nodeid]:
                # settled nodes are already optimal
                # no need to add them again.
                # this is not needed
                # if settled[dest] >= 0:
                #     continue
                heapq.heappush(heap, (dist + w, dest))


        # convert inf to -1        
        return {i:settled[i] for i in range(n)}
                




            


