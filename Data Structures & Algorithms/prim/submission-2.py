import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        ## plan.
        ## grow the tree one node (and edge) at a time.
        ## track the total size
        ## pick arbitrary starting point.
        ## add its smallest edge
        ## now pick the smallest outgoing edge from the set.
        ## state
        if n == 0:
            return 0

        remaining = [True for _ in range(n)] # set of vertices not yet explored 
        num_remaining = n

        adjacency = [[] for _ in range(n)] 
        for (u, v, w) in edges:
            adjacency[u].append((w, v))
            adjacency[v].append((w, u))

        region_edges = []
        total_weight = 0
        next_vertex = 0
        while num_remaining > 0:
            # pick any vertex
            remaining[next_vertex] = False
            num_remaining -= 1

            # add its edges to region edges
            for (w,dest) in adjacency[next_vertex]:
                if remaining[dest]:
                    heapq.heappush(region_edges, (w, (next_vertex,dest)))
             
            # check for next min edge out:
            found_next = False
            while region_edges:
                (w, (src, dest)) = heapq.heappop(region_edges)
                if remaining[dest]:
                    total_weight += w
                    next_vertex = dest
                    found_next = True 
                    break
            
            # continue loop only if we have a next edge
            if not found_next and num_remaining > 0:
                return -1 # no outgoing edges to remaining node


        return total_weight











        