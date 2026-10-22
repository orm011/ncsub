
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # next approach. build a graph first, then traverse the graph.
        # nodes: the position of the account
        # edges: node a and b are connected if they overlap through some address
        n = len(accounts)
        acc2node = defaultdict(set)
        graph = defaultdict(set)
        for i, acct in enumerate(accounts):
            for addr in acct[1:]:
                for j in acc2node[addr]:
                    graph[i].add(j)
                    graph[j].add(i)
                
                acc2node[addr].add(i)

        output = []
        curr = []
        added = [False for _ in range(n)] # set to true when added to stack the first time
        remaining = set(range(n))
        outputid = [None for _ in range(n)]
        stack = []

        inputid = []
        while True: # dfs of the graph
            if not stack and len(remaining) == 0:
                break # done
            elif not stack and  len(remaining) > 0: # stack empty but graph not
                node1 = next(iter(remaining))
                remaining.remove(node1)
                added[node1] = True
                oid = len(output) # position in output
                outputid[node1] = oid #
                output.append(set())
                inputid.append(node1) # map from outputid to input to track the name
            else: 
                node1 = stack.pop()
                oid = outputid[node1]

            # add all nodes to output
            for accname in accounts[node1][1:]:
                output[oid].add(accname)

            # move on to graph
            for node2 in graph[node1]:
                if not added[node2]: 
                    stack.append(node2)
                    added[node2] = True
                    remaining.remove(node2)
                    outputid[node2] = outputid[node1] # same output

        final_outputs = []
        for oid, accs in enumerate(output):
            iid = inputid[oid]
            final_outputs.append([accounts[iid][0]]) # name
            for acc in sorted(accs):
                final_outputs[-1].append(acc)

        return final_outputs

        





                
