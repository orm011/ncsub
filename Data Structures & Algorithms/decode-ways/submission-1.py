class Solution:
    def numDecodings(self, s: str) -> int:
        # largest number: "26"
        # so, all possible ambiguities arise from
        # "11 ... 19", then "21...26" (10 and 20 are not ambiguous, nor are 27, 28, 29, and all 3*)
        # if we see 19 next, we just multiplied by 2 possible decodes (full 19, 1, 9)
        #  then we move forward 9 can only be alone.
        # if we see 11 next. we multiplied by 2 possible decodes. then next step:
        # we see the second 1, it may have again multiple decodes 
        #"111" => 1,1,1 or 11,1 or 1,11.

        # recurrence option:
        # check next character:  if valid standalone, consider all possible decodings of the rest. w/o that char.
        # check next two characters: if valid together, consider all possible decodings of the rest after it.
        # sum them to get the totals
        n = len(s)
        memoized = [-1 for _ in s]
        def dp(i: int):
            if i == n:
                return 1 # need to be 1 so that a 26 returns 2 options.
            if i == n - 1: # last char
                return 0 if s[i] == '0' else 1  

            if memoized[i] != -1:
                return memoized[i]

            if s[i] == '0':
                memoized[i] = 0
                return 0
            
            res1 = dp(i+1)

            res2 = 0
            if s[i] == '1':
                res2 = dp(i+2) # '10' to '19'
            elif s[i] == '2' and s[i+1] not in ['7', '8', '9']:
                res2 = dp(i+2) # '20' to '26' 
            else:
                pass
            memoized[i] = res1 + res2
            return memoized[i]

        return dp(0)


        