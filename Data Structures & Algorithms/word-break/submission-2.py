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

        def startswith(i) -> Iterator[int]: # returns all possible starting matches of s[i:] with words of wordDict, returns list of offsets. s[i:i+o]
        # is a match. empty list means no matches.
            # initial impl: cost is O(n) + O(M) # initial copy of suffix.
            for w in wordDict:
                if s.startswith(w, i):
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
                b[pos] = True
            
        
        # complexity: 
        # n iterations. each is doing an O(n) string copy and a 
        # O(M) match (char by char comparison)
        # O(n * (n + M))
        # space: array b is O(n). 

        # can reduce O(n * (n+M)) to O(n*M) by comparing string chars manually in stead of substring + startswith.
        # if we build a Trie on wordDict, O(M) time, O(M) space,
        # we can do O(n * (m_max + m)), ie, match all at the same time, continue until largest match, still making m writes to array in case 


        # recursive formulation: 
        # rec(k) means -k: is doable.
        return b[n]

                
        

            
            
        

        