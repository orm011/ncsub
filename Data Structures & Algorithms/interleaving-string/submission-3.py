class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # isInterleave(s1[:k+1], s2[:h+1], s3[:k+h+1]) = 
        # isInterleave(s1[:k], s2[:h+1], s3[:k+h]) and s1[k] == s3[k+h]
        # or isInterleave(s1[:k+1], s2[:h], s3[:k+h]) and s2[h] = s3[k+h]
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False

        memoized = {} # maps (i1, i2) -> bool

        def dp(i1, i2, i3) -> bool:
            # try first:
            if i3 == n3:
                return True

            if (i1,i2) in memoized:
                return memoized[(i1,i2)]

            if (i1 < n1 and s1[i1] == s3[i3] and dp(i1+1, i2, i3+1)):
                memoized[(i1,i2)] = True
                return True

            ans = (i2 < n2 and s2[i2] == s3[i3] and dp(i1, i2+1, i3+1))
            memoized[(i1,i2)] = ans
            return ans
            
        return dp(0, 0, 0)
        