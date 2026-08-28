class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # strategy: 
        # this is a topological sort problem, prereqs are the edges.
        # build an adjacency list: node -> prereqs.
        # then search for roots (no prereqs) and so on (Kahn's algorithm)
        prereqs = [0 for _ in range(numCourses)] # mapping i -> # prereqs of i
        postreqs = [[] for _ in range(numCourses)] 
        # mapping j -> courses that directly depend on j
        
        for [c, p] in prerequisites:
            prereqs[c] += 1
            postreqs[p].append(c)

        # keep track of nodes with empty prereqs. 
        # remove them, and update all nodes with that prereq.
        # question: at every step we want to find the nodes with
        # empty prereqs without full scan.
        # we can find out which are zero when we update counts
        pending = [] # nodes with 0 count not removed yet.
        # initialize pending
        for i in range(numCourses):
            if prereqs[i] == 0:
                pending.append(i)

        output = []
        while pending:
            node = pending.pop()
            output.append(node)
            for i in postreqs[node]:
                prereqs[i] -= 1
                if prereqs[i] == 0:
                    pending.append(i)
        
        if len(output) == numCourses: # if all courses made it, 
            return output
        else:
            return []

    # complexity: 
    # create structure with numCourses, scan prereqs:
    # time O(V + E)
    # then while  loop runs over nodes, and each over edges
    # so again O(V + E)
    # total O(V+E)
    # auxiliary space: O(V + E)

        


        


        