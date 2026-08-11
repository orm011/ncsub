"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # need to traverse every reachable node, 
        # but when finding any already copyied nodes, 
        # we should use the existing copy instead of making a new one.
        # we can do this via DFS, it will visit every node in the graph
        seen = {} # map of node id to Node object
        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None    
            elif node.val in seen:
                return seen[node.val]
            
            # first time:
            new_node = Node(val=node.val)
            seen[node.val] = new_node # downstream edges can refer to this

            for n in node.neighbors:
                new_n = dfs(n)
                new_node.neighbors.append(new_n)
            
            return new_node

        return dfs(node)
        # complexity:
        # stack size: longest path in graph, could be large, O(E)
        # time: number of edges O(E)
        # space: O(E) as well, unavoidable since we are doing a copy


        
        