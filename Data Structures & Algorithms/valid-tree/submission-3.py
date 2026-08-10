from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        for [u,v] in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        # can start dfs at one node, and should get to every 
        # point, without cycles.
        visited = set([0]) # reached by some path before.
        source = None
        edgestack = [(0, k) for k in adjacency[0]]
        cyclefound = False
        path = [None, 0] # stack need a stack of nodes
        while edgestack:
            (curr, maybenode) = edgestack.pop()
            while curr != path[-1]:
                path.pop()
            if maybenode in visited:
                cyclefound = True
                break
            
            edgestack.extend([(maybenode, n) for n in adjacency[maybenode]
            if n != curr])
            path.append(maybenode)
            visited.add(maybenode)




        return not cyclefound and len(visited) == n
