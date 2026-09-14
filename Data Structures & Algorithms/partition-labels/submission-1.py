class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # worst case scenario everything is one string.
        # but we may be able to get more substrings than that.
        # what is the condition that would allow more than one?
        # there exists some position such that the two substrings
        # are disjoint (in terms of constituent chars)
        # this reasoning applies recursively.
        #  a maximal split would have every part be disjoint, and 
        # would allow no more sub-partitionings
        # because of the recursive sub-structure, lets define more formally
        n = len(s)
        # best[n] := the best partitioning of the string starting from 0 to n, expressed as the output array of lengths
        # best[k] from 0 to k
        # then:
        # smallest_string(n)
        # best[n] = [len(smallest_string(n))] + best(n - len(smallest_string(n))) 
        # is there ever a case where we should not be greedy (smallest string).
        # no, bc we could split that first string and get a better split, since that first string is by def disjoint with the rest.
        
        # if we go left to right, how do we know when to stop. only when we know none of the active characters is repeated again.
        # how do we answer that query fast?
        # lets keep counts of all chars.
        from collections import Counter
        counter = Counter(s)
        active = set() # which we have seen in the current open substring.
        output = [] # -1 is always current count
        for i in range(n):
            # strategy: we track an active set, elements we have seen that have non negative count.
            # we should close the current substring if this active set becomes empty.
            if not active: # new beginning
                output.append(0) # current count

            c = s[i]
            active.add(c)
            counter[c] -= 1
            output[-1]+=1
            
            if counter[c] == 0:
                active.remove(c)

        return output


            