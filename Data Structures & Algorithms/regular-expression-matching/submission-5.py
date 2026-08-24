class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # solve recursively moving the indices forward
        # when p  starts with a literal character, it must
        # match exactly (not directly followed by *)
        # whe p starts with a ., it can match anything on the left,
        # just move the left forward
        # when p starts with a char followed by a *, it will match empty
        # or as much as possible of the repeated char
        # .* is allowed, and it matches anything (not necessarily repeated)... so the thing here is picking whatever lets the next chars match.
        # how about situations like n*nn, and we have
        # a string like nn. then n* should match empty. 
        n = len(s)
        m = len(p)

        # limited subproblems: therefore
        memoized = {(n,m): True}
        def rec(i: int, j: int) -> bool:
            # print(f"{i=} {j=} {n=} {m=} {s[i:]}, {p[j:]}")
            ans = memoized.get((i,j))
            if ans is not None:
                return ans

            # handle star pattern
            if j + 1 < m and p[j+1] == '*':
                # for .* need one handle.
                # for a* need to consider all possible lengths.
                # consider matching none of s
                if rec(i, j+2):
                    ans = True
                # consider matching 1 or more of s
                elif i < n and (p[j] == "." or s[i] == p[j]):
                    ans =  rec(i+1, j)
                    #print(f"matching one or more {i=} {j=}: {ans=}")
                else: # mismatch
                    #print(f"{i=}{j=}{s[i]=} {p[j]=}")
                    ans = False
            elif j < m and i < n and (p[j] == "." or s[i] == p[j]):
                # consume one
                ans = rec(i+1, j+1)
            elif j == m and i == n:
                ans = True
            else:  # either j == m and i < n, or vice versa,
            # and already know no star pattern
                ans = False

            memoized[(i,j)] = ans
            return ans

            
        return rec(0,0)

        # initial apporach: recursive matchgin with memoization.

            



        