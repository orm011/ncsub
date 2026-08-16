from collections import defaultdict
import graphlib

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # strings of words are sorted lexicographic by alien rules.
        # supposedly.  is it consistent?
        # if it is returns some solution.
        # 
        # lexicographic: charwise, then by shorter.

        # for each pair of words, we learn one fact about the ordering
        # from the first unequal character, if they differ, or else we
        # check the ordering by shorter.

        # rough idea: graph datastructure adds directed edges between
        # characters.
        # any topological sort of this structure corresponds to a 
        # valid char order based on the constraints.
        # if there is a cycle, or if the shorter precedes longer part does not 
        # hold, then there is no possible ordering.
        nwords = len(words)

        edges = defaultdict(set)
        prev = words[0]
        
        for c in prev:
            edges[c]
        for i in range(1, nwords):
            curr = words[i]
            prefix = True
            for j in range(len(curr)):
                ccurr = curr[j]
                edges[ccurr] # add to dict

                if prefix and j < len(prev) and prev[j] != ccurr:
                    edges[prev[j]].add(ccurr)
                    prefix = False
                

            if prefix and len(prev) > len(curr):
                return ""
            
            prev = curr
            # print(f"{i=} {dict(edges)=} {prev=} {curr=}")
        sorter = graphlib.TopologicalSorter(edges)

        # some observed characters never appear in the graph as keys
        # or values, if they never break ties. 
        # Those can be in any order

        try: 
            ordered = list(sorter.static_order())
        except graphlib.CycleError as e:
            print(f"CycleError: {e}")
            return ""
        
        ordered.reverse()
        return ''.join(ordered)


        # to get an ordering or find out there is none
        # we need to do a top sort. 


            
