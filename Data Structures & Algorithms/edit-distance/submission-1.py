class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## possible approaches
        ## compare the first two chars for both.
        ## if equal, we only need the min distance of the suffixes.
        ## if not equal then there are multiple things that could happen next.
        ## a) substitution in word1 plus the min distance of suffixes
        ## b) deletion of that position in word1, plus min distance of that suffix.
        ## c) insertion of the match, plus min distance of suffixes.
        results = [ [-1 for _ in range(len(word2) + 1)] 
                        for _ in range(len(word1) + 1) ]


        def dfs(memoized: list[list[int]], suffix1: str, suffix2: str):
            if len(suffix1) == 0:
                memoized[len(suffix1)][len(suffix2)] = len(suffix2)
                return len(suffix2) # insertion is only option to match word2
            elif len(suffix2) == 0:
                memoized[len(suffix1)][len(suffix2)] = len(suffix1)
                return len(suffix1) # deletions only option here
            else:
                pass

            maybe_ans = memoized[len(suffix1)][len(suffix2)]
            if maybe_ans != -1:
                return maybe_ans

            c1 = suffix1[0]
            c2 = suffix2[0]
            if c1 == c2: # matches, no operation needed
                ans =  dfs(memoized, suffix1[1:], suffix2[1:])
            else:
                # options: replace, delete or insert
                replace_cost = 1 + dfs(memoized, suffix1[1:], suffix2[1:])
                delete_cost = 1 + dfs(memoized, suffix1[1:], suffix2)
                insert_cost = 1 + dfs(memoized, suffix1, suffix2[1:])
                ans = min(replace_cost, delete_cost, insert_cost)

            memoized[len(suffix1)][len(suffix2)] = ans
            return ans
        
        return dfs(results, word1, word2)
            

            
