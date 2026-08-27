from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # JFK is the starting point
        # we want to use all edges, they are directed.
        # start with JFK but chose next step so that it is possible to use them
        # all up, there is at least one option.
        # if there are more, then pick the lexicographically smaller one.
        
        # representation: tickets are a directed graph,
        # DFS can find the longest path (no repeated edges) in a directed graph.
        # if we always choose edges by alphabetic order, the first path 
        edges = defaultdict(list)
        n = len(tickets)
        for (src,dest) in sorted(tickets): # this will append in order
            edges[src].append(dest)
        
        # print(edges)

        stack = [(None,"JFK",0)]
        # current path
        pathset = set() # set of edges
        path = [] # sequence of edges.
        # now do a DFS
        # note: should not use the same edge twice, but may need to visit the same
        # node multiple times (see second example)
        # actually can use the same edge twice, just not the same ticket.
        while stack:
            # print(f"{stack=}\n{path=}\n{len(pathset)=}\n{pathset=}")
            (src,node,idx) = stack.pop()
            # taking the node means adding this to path:
            while path and path[-1][1] != src: 
                elt = path.pop() # we are now exploring a different path.
                pathset.remove(elt)

            if (src,node,idx) in pathset:
                # we are looping, do not explore this path further.
                continue
            
            # add to path
            path.append((src,node,idx))
            pathset.add((src,node,idx)) 

            if len(pathset) == n + 1: # reached full set
                return [dst for (_,dst,_) in path] # skip the None
            for idx,dst in enumerate(edges[node][::-1]):
                # go by reverse order so we visit lowest name first
                stack.append((node,dst,idx))
                # remaining question: how do we remove from path.    


