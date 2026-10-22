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
                if settled[dest] >= 0:
                    continue
                heapq.heappush(heap, (dist + w, dest))


        # runtime here:
        # Each node runs through the long loop once. 
        # each loop run does at most work prop to the number of edges.
        # the loop itself runs  as many times as there are
        # things added to the heap, which is number of edges.
        # time: O(E)  
        # space: O(E) as well
        # answer has entry for each vertex, so O(V)

        # lets think of graph [[0, 1, 1], [0, 2, 3], [1,2,1], [2,1,0]]
        # answer should be [0:0, 1:1, 2:2]. 
        # start with 0. this expands answer. marks 0.
        # adds (1, 1) and (0+3, 2) to heap.
        # next round gets (1,1)... not visited yet 
        # mark it with 1, and then expand.
        # adds (1+1, 2) to the heap. 
        # next pop gets (2,2) out. 
        # adds the node (2 + 0, 1) out.
        # this edge is to 1, which has already been settled.
        # it gets ignored. no more visits to 1.




        return {i:settled[i] for i in range(n)}
                




            


