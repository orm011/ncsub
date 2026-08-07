class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # interesting problem...
        # loop solution:
        # for every position in the string, check which dictionary words fully match.
        # for each pos in the string, for each word in dictionary, get which match.
        # then do what? still need to make choices about which combination creates the
        # smallest residual.

        # lets consider the first character in the string.
        # if it is not the first in any dictionary word, then it cannot be in the partition.
        # then we can recurse on the remaining string s[1:] and find the minimal residual there.
        # if there is a match with several dictionary words, then we can find the best
        # residual for the remaning string after. we still want to consider not using
        # that character
        # how do we test for teh match with dictionary words? 
        # option 1 is loop.

        memoized = {}
        def dfs(s: str) -> int:
            if s == "": 
                return 0
            elif s in memoized:
                return memoized[s]

            options = set() # always include remainder of 1
            for word in dictionary:
                if s.startswith(word):
                    options.add((len(word)))

            
            if 1 in options:
                first_char_residual = 0
            else:
                options.add(1) # still need the subproblem
                first_char_residual = 1

            results = []
            for start in options:
                mc = dfs(s[start:])
                if start == 1:
                    results.append(mc + first_char_residual)
                else:
                    results.append(mc)
                    # first char residual only applies to the case of starting at 1

            # print(f"{s=} {first_char_residual=}")
            ans  = min(results)
            memoized[s] = ans
            return ans
        return dfs(s)
        # how do i know if the 1 in options is bc of a match or bc give up.
        # if there is a match, we will always prefer it.
        # otherwise we will add a 1.




        

