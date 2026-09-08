class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # string and dict of words
        # can we segment string fully.
        # thoughts:
        # some easy cases: we cannot match any of the words in the dict
        # at current point in the string, or we can match exactly one.
        # harder: we can match multiple strings in the dict
        # can work on string left to right or right to left.

        # let b(k) whether the string starting at s[:k] can be broken
        # into words from wordDict.
        # b(n) is the answer to our problem.
        # b(0) is always true
        # b(1) depends on dict.
        n = len(s)
        m = len(wordDict)
        # M = sum of lengths of words in 
        # b(n) is equivalent to
        # there exists a w with startswith(s, w in wordDict) and s(n-len(w))
        # this forces us to try potentially a bunch of words that match,
        # and their subproblems, O(m * n) in time.
        b = [False for _ in range(n + 1)] # s[n]
        b[0] = True

        def startswith(i) -> list[int]: # returns all possible starting matches of s[i:] with words of wordDict, returns list of offsets. s[i:i+o]
        # is a match. empty list means no matches.
            # initial impl: cost is O(n) + O(M) # initial copy of suffix.
            suffix = s[i:] 
            for w in wordDict:
                if suffix.startswith(w):
                    yield len(w)

        for i in range(0,n+1):
            if b[n]: 
                # check if previous round got to n.
                return True

            if not b[i]: 
                # if no previous round got here, this cannot build up.
                continue

            # s[i] is true, which other can we build
            for offset in startswith(i):
                pos = i + offset
                if pos < n + 1:
                    b[pos] = True
            
        return b[n]

                
        

            
            
        

        