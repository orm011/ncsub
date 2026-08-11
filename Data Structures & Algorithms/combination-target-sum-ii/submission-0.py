from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # unique combination means
        # we do not care about the ordering of the members
        # ie there are 2^n combinations 
        # (bit 0 or 1 for whether we use a position)
        # some of them sum to the target. 
        # notice: actually there are fewer
        # bc [1,2,5] could have come from either 2, but only
        # counts as one. whereas the bit vector would only 
        # look at indices.

        # les assume unique entries with counts for how many appearances. (initial pass with counter)

        # for each of these values, we can choose to use it
        # either 0 or at one or more times.
        # C(n+1, target) =  C(n, target) + C(n, target - c[n])
        # + C(n , target - 2*(c[n])) .. + 

        # implementing this recurrence directly 
        # gives us an O(n*T) dynamic programming solution.
        # an n * T grid, each element takes O(1) to fill
        # with a similar amount of space. 
        summary = Counter(candidates) # O(c) 
        # entries in candidates

        uniques = []
        count = []
        for (k,v) in summary.items():
            uniques.append(k)
            count.append(v)
        
        # prev_dp = [0 for _ in range(target + 1)]
        # dp = [0 for _ in range(target + 1)]
        
        prev_solns = None
        solns = [[] for _ in range(target + 1)]
        solns[0] = [[]] # one unique empty solution



        # tracking solutions
        # dp[len(uniques)][target] is the answer
        # dp[k][0] = 1, can always choose not to use         
        # prev_dp[0] = 1
        # dp[0] = 1

        for coinpos in range(0,len(count)):
            prev_solns = solns
            solns = [[] for _ in range(target+1)]
            solns[0] = [[]]
            for target_val in range(1,target+1):
                denom = uniques[coinpos] # s=1 maps to first unique
                for i in range(count[coinpos] + 1):
                    sol = prev_solns[target_val - i*denom] if target_val - i*denom >= 0 else []
                    
                    for s in sol:
                        s1 = s.copy()
                        s1.extend([denom]*i)
                        solns[target_val].append(s1)

                # to get the final sequence. 
                # within the loop.. each prelim implies
                # a choice of adding the coin i times to 
                # the set of solutions for
                # dp[coinpos - 1][ target_val - i * denom ]
                # if we materialize these naively, 
                # we could have a space blow up: O(target*c*(large lists))
                # 
        return solns[-1]