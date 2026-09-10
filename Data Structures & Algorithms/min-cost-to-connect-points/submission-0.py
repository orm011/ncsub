import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # manhattan distance: sum of diff.
        # connecting all points together at minimal cost is 
        # a kind of minimal spanning tree problem.
        # The solution has O(n) size.
        # The input problem has O(n) size (points)
        # one annoying thing is the full graph has O(n**2)
        # the msp algorithm, like prim, at every step add the minimal 
        # size outgoing edge to expand the tree.
        # alternative, kruksal, is to add globally the smallest edge that
        # does not cause cycles
        # impl alternative 1: materialize the n**2 edges and apply either 
        # algorithm. 
        # time: O(n**2) to build graph and then O(n**2 log n) to build


        # the tree. We can skip the initial build by late-materialzing edges only from new point to left over nodes. 

        n = len(points)

        edges = []
        nodes = set([0])
        leftover = set(range(1,n))
        total = 0
        queue = []

        # add edges
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def add_edges(n0):
            for n1 in leftover:
                w = dist(points[n0], points[n1])
                heapq.heappush(queue, (w, (n0, n1)))

        add_edges(0)
        while len(edges) < n - 1:
            nextnode = None
            while nextnode is None:
                (w, (n0, n1)) = heapq.heappop(queue)
                if n1 in leftover:
                    nextnode = n1

            nodes.add(nextnode)
            edges.append([n0, n1])
            total += w
            leftover.remove(nextnode)
            add_edges(nextnode)

        return total
        
            






        

        
        

