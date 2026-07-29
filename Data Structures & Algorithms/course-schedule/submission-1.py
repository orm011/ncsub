from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## edges [a,b] means b (before) needed before a
        ## can finish everything if there is no cycle ie, 
        ## if it is possible to topo-sort.
        # option1: attempt to find out if there is a loop, eg via bfs.
        # option2: attempt to sort this topologically
        ## we do not know which vertex to start from, so need to handle any.
        ## we do know about edges, and can index by vertex.
        ## can pick a vertex and add traverse its edges, adding them as we go, and tracking
        ## visited nodes. 
        ## if by traversing edges, we point to a visited node, we found a cycle, answer is negative.
        ## if we run out of edges, answer is positive

        ## problem. with 1 -> 0. if i visit 0 first, 

        inedgemap = defaultdict(list)
        outedgemap = defaultdict(list)

        for (a, b) in prerequisites:
            inedgemap[a].append(b)
            outedgemap[b].append(a)
        
        nodes_removed = set()
        
        sources = []
        for i in range(numCourses):
            if len(inedgemap[i]) == 0:
                sources.append(i)

        #print(f"{sources=} {nodes_removed=} {inedgemap=} {outedgemap=}")        
        while len(nodes_removed) < numCourses:
            if len(sources) == 0:
                return False
            else:
                newsources = []
                for s in sources:
                    nodes_removed.add(s)
                    for k in outedgemap[s]:
                        inedgemap[k].remove(s)
                        if len(inedgemap[k]) == 0:
                            newsources.append(k)

                    del inedgemap[s]
                sources = newsources
                #print(f"{sources=} {nodes_removed=} {inedgemap=} {outedgemap=}")        

        
        #print(f"{sources=} {nodes_removed=} {inedgemap=} {outedgemap=}")        
        return True
        
        
        # visited everything
        # any leftover vertices mean loop. wrong. eg [0,1].
        # pick 0. mark as visited. 
        # pick 1. now need to visit 0. this edge goes to a visited node, yet
        # there is no loop here.
        # [[0,1],[1,0]]
        # pick 0. mark as visited.
        # there is [0,1]
        # 1 is next. mark visited. 
        # 1 was added via edge from 0, not from nowhere.
        # now we go [0,1]. visited. 
        # not necessarily. its only a loop if we arrived that that visited
        # node via an edge, not if we picked it up arbitrarily.

        ## no easy way to fix. we could pick something in the middle, traverse.
        ## plan2: lets be careful what we pick as starting point.
        ## we pick a node with in-degree 0. if none available, we have our answer.
        # we follow the same plan... does not work bc consider 0 -> 1 , 2->1.
        # no loop but visit 1 twice.
        #
        # new idea: find all vertices with in degree 0. those are roots.
        # those are always doable, no cycle can go through them.
        # now we just need to think of the graph that remains if we remove these and their outedges.
        # now look again. find new roots. if there is none, then there is a cycle.