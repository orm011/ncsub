class Solution:
    def countSubstrings(self, s: str) -> int:

        # reducing space to O(1) by increasing locality in our access pattern
        # evens: do (i,i+1), (i-1,i+2) so on (starting at diagonal, go up to the
        # right.
        n = len(s)

        total = n # already include each individual letter


        # odd entries
        for i in range(n): # represents positions (i,i+1)
            #print(f"{i=} {1,min(i + 1, n - i)=}")
            for d in range(1,min(i + 1, n - i)): # smallest dist to either end.
                # eg i = 0: 0,1 only used once. Range should end at 1.
                # eg i = n - 1. same, range should end at 1
                # min(n - 1 + 1, n - n + 1): 1.
                # need start , end 0,2
                # i = 1. => start = 0, end = 2.

                # min(1 + 1, 3 - 1) = 2. range(1,2).
                start = i - d
                end = i + 1 + d   
                if s[start] == s[end - 1]:
                   # print(f"{(start,end)=}")
                    total += 1
                else: 
                    break # no more need.
        
       # print(f"after odds: {total=}")
        # even entries # [i,i+2]
        for i in range(n-1): # stops at n-2:n
            for d in range(0, min(i+1, n - i - 1)): 
                # i=0=> i:i+2 counts, but cannot grow. range must eq 1.
                # min(0+1, n-0) is 1.
                # i = n - 2 when d is 0: s[n-2] == s[n +1 ]
                # min(n - 2 + 1, n - n + 2) 
                # min (n -1, 2)
                start = i - d
                end = i + 1 + d
                # print(f"{(start,end)=}")
                if s[start] == s[end]:
                    total +=1
                else:
                    break

        return total