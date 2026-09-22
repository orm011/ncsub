import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # shortest time until everything is connected.
        # can we do this with something like dijkstra,
        # where instead of having a target node and stopping when 
        # we hit it, we stop when every node is visited.
        # dijkstra grows the visited set by adding the nearest next node
        # (to anyone in the set).
        # invariant: the paths to everyone in the set are the shortest paths
        # from that source.
        
        edges = defaultdict(list)
        for (u, v, t) in times:
            edges[u].append((v, t))
        
        heap = [(t, k, v) for (v,t) in edges[k]] # (distance, nodeid)
        heapq.heapify(heap)

        visited = [(True if i == k else False) for i in range(n+1)]
        totalvisited = 1

        mintimes = [0 for _ in range(n+1)] # track shortest distance to each
        maxtime = 0 # max(mintimes)
        while True:
            #print(f"{heap=}")
            found = False
            while heap:
                (t, u, v) = heapq.heappop(heap)
                if not visited[v]:
                    found = True
                    break

            if not found: # done
                break

            assert visited[u] and not visited[v]
            mintimes[v] = t
            #print(f"{u=} {v=} {mintimes[v]=} {maxtime=} ")
            # is the formula correct? 
            # the time needed to get to v is the time needed to get to u
            # plus the delay on that last link.
            # my output is larger than the reference.
            # where is this happening

            # there is a link 5->4 that takes 31 exactly.
            # whereas we are going from 3->4 15 + 22 = 37.
            # so our choice is wrong.
            # I'm doing an MSP here, i think, not shortest path..

            maxtime = mintimes[v] # probably redundant

            # add edges to heap
            for (destv, t) in edges[v]:
                # use the full time so far.
                heapq.heappush(heap, (mintimes[v] + t, v, destv))
            
            visited[v] = True
            totalvisited += 1
        
        # heap empty
        if totalvisited < n:
            return -1 # unreachable
        else: 
            return maxtime








        