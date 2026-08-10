from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree has no loops, and every vertex is connected.
        # (ie has a single connected component)
        # necessary condition:
        # there are n-1 edges, and every node is in at least one edge.
        # is this sufficient?
        # can there be a cycle: if there is one, remove one edge from it.
        # everything remain connected, yet edge count smaller. hence the count could not be n in the first place.
        # unless it was not connected in the first place...

        # can we add check for connectedness.

        if len(edges) != n - 1:
            return False
        
        adjacency = defaultdict(list)
        for [u,v] in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        # can start dfs at one node, and should get to every 
        # point, without cycles.
        visited = set() # reached by some path before.
        def dfs(n: int, source: int) -> bool:
            """will traverse from node n, returning only when it has traversed everything reachable, excluding coming back to source. Returns False if there is a cycle """

            visited.add(n)

            for neighbor in adjacency[n]:
                if neighbor == source:
                    continue
                if neighbor in visited: # this means we are back
                # at a previously visited node, not through the back edge.
                # this means there is a path to that node different from the one originally taken... some questions here though. 
                    return False
                
                ok = dfs(neighbor, n)
                if not ok:
                    return False
                

            return True

        ok = dfs(0, None)
        return ok and len(visited) == n