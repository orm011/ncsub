class Solution:
    def countSubstrings(self, s: str) -> int:
        # lets explore the idea of counting substrings
        # by re-using as much as possible existing palindromes 
        # and growing them
        n = len(s)

        # pali(i, j) := the substring between s[i:j] is a palindrome.
        # if i == j, empty string.
        # naive approach:
        # for i
        #   for j
        #.     check(i,j), add to total.
        # O(n**3) cost.
        # work not re-used.
        # check(i,j) = (s[i] == s[j-1]) and check(i+1, j-1)
        # also, if !check(i+1, j-1) then can mark everything else
        check = [[-1 for _ in range(n + 1)] for _ in range(n+1)]

        # note final answer needs to be counts.
        # counts[i][j]: # total number of pali in that substring.
        # plan: build the array. diag by diag:
        total = 0
        for delta in range(0, n+1): # gap between delta
        # 0 to check[1][1] empty string, n cases like this
            for i in range(0, n + 1 - delta):
            # delta n corresponds to check[0][0+n], of which three is only one
            # delta 0 will range from [0][0] to [n][n]
            # delta 1 will range from [0][1] to [n-1][n] which is what we want.
                j = i + delta
                if delta == 0: # empty base case. does not count.
                    check[i][j] = 1
                elif delta == 1: # single char case. always true, counts
                    check[i][j] = 1
                    total += 1 
                else:
                    check[i][j] = check[i+1][j-1] and s[i] == s[j-1]
                    total += check[i][j]

        return total


        
