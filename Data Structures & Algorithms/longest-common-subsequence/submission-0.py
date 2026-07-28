from collections import defaultdict

def findlastpos(text, c):
    ans = None
    for i,cc in enumerate(text):
        if cc == c:
            ans = i
    return ans

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # how to think about this problem.
        # longest common subsequence between text1 and text2[:i].
        # how do we cast the solution in terms of the solution to a smaller problem.
        ## text2 empty: then empty
        ## text2 one char: then 0 if char in text1, 1 o/w
        ## text2 2 chars: could be 0, 1, 2 depending.
        ## text2 k chars. is text2[-1] in the longest. 
        ## find the longest for text2[:-1]. then if text2[-1] appears after the last letter in text1, that must be
        ## the longest. if text[-1] does not appear at all in text1, then that must be the longest as well.
        ## however, if text[-1] appears somewhere in text1 (pos k), the question is whether we should consider the longest subsequence
        ##  text1[:k], text2[:-1] and add text[-1] to it. that would offer an alternative.

        ## if i know the length for the longest subseq for text1[:h] and text2[:k]
        ## then for text1[:h+1], text2[:k] we find the longest one way
        ## and text1[:h], text2[:k+1] as we did above.

        ## find the last char c of text2 within text1. all the positions.
        # if empty: no solution can have it.
        # if one position $x$: the best solution including the last char would extend text1[:x], text2[:j].
        # if multiple positions: does it matter? we just need the best possible sequence at [i,j]. we know 
        # lcs[i,j] >= lcs[h,k] whenever i>=h and j>=k.

        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return 0
        
        # initialize
        # option 1:
        # lcs[i][j] holds the length of the LCS between text1[:i] and text2[:j], ie excludes char i.
        # answer will be lcs[m][n]
        # lcs[0][0] = 0 since both are empty. lcs[0][j] also 0
        # needs to be of length m+1 by n+1
        # option 2: what we currently do.
        # lcs[i][j] holds the length of the lcs between text1[:i+1] and text2[:j+1] includes char j
        # answer will be lcs[m-1][n-1]
        # lcs[0][0] = depends on char equality.
        # i could be 0, and lastindex could be 0, in which case we index into -1

        lcs = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    lcs[0][0] = int(text1[0] == text2[0])
                    #position[0,0] = (0,0) if not lcs[0][0] else (1,1)
                    continue
                
                # then, longest subsequence
                # look for the longest excluding the last text2 char
                # h,k = pos[i][j-1]
                prevlen = lcs[i][j-1] if j > 0 else 0
                lastchar = text2[j]
                lastpos = findlastpos(text1[:i+1], lastchar) # note lcs0,0 includes char 0. 
                # 0 <= lastpos <= i 
                if lastpos is None:
                    # lastchar cannot be part of subseq
                    # pos[i][j] = (h,k) # same ans as previous.
                    lcs[i][j] = prevlen # same ans as previous.
                else:
                    # consider matching on that last char at text1[lastpos]
                    option2lcs = lcs[lastpos-1][j-1] if (lastpos > 0 and j > 0) else 0
                    optionlen2 = option2lcs + 1
                    if optionlen2 > prevlen:
                        # pos[i][j] = (lastpos, j)
                        lcs[i][j] = optionlen2
                    else:
                        # pos[i][j] = (h,k)
                        lcs[i][j] = prevlen

                # remains to do: 
                # make sure we can handle indexing on[lastpos-1] and [j-1]
                # indexing. set clear convention
                # no need for pos array anymore it seems.
        return lcs[m-1][n-1]
