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
        memoized = {}
        def rec(i: int, j: int) -> bool:
            # print(f"{i=} {j=} {n=} {m=} {s[i:]}, {p[j:]}")
            ans = memoized.get((i,j))
            if ans is not None:
                return ans
        
            # current impl has can be rewritten with fewer cases
            if i == n: # either empty or star pattern a*b*c*
                if j == m:
                    ans = True
                    memoized[(i,j)] = ans
                    return ans         
                elif j + 1 < m and p[j+1] == '*':
                    ans = rec(i, j+2)
                    memoized[(i,j)] = ans
                    return ans
                else: 
                    # s is done, p is not done and its not a star pattern
                    ans = False
                    memoized[(i,j)] = ans
                    return ans
            elif j == m:
                ans = False
                memoized[(i,j)] = ans
                return ans

            assert i < n and j < m, f"{i=} {j=}"
            # no star coming:
            if j + 1 == m or (j + 1 < m and p[j+1] != '*'):
                ans = ((p[j] == "." or s[i] == p[j]) # consume one
                        and rec(i+1, j+1))
            else:
                # for .* need one handle.
                # for a* need to consider all possible lengths.
                
                # consider matching none of s
                if rec(i, j+2):
                    ans = True
                # consider matching 1 or more of s
                elif p[j] == "." or s[i] == p[j]:
                    ans =  rec(i+1, j)
                    #print(f"matching one or more {i=} {j=}: {ans=}")
                else: # mismatch
                    #print(f"{i=}{j=}{s[i]=} {p[j]=}")
                    ans = False

            memoized[(i,j)] = ans
            return ans

            

        return rec(0,0)



            



        