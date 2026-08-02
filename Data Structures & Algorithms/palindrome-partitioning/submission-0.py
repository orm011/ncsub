class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # partition means it needs to split neatly into these.
        # since a single char is always a palindrome, 
        # there is always the list of chars for any string.

        # lets consider the problem of counting the number of partitionings
        # for a string of length n + 1
        # we can decompose this problem into 
        # the number of partitionings for string of length n (since alst char is also
        # a palindrome).
        # plus, the number of partitionings of length n-1 (only in case the last two chars are a palindrome
        # P(n+1) = P(n)*p(n+1)?  + P(n-1)*p(n:) + P(n - 2)*p(n-1:)...
        # the second factor is a boolean.
        # Q: are we double counting.
        # we know the last char must be included in a palindrome.
        # hence we know the overall partitioning is unique.

        # suggested apporach:
        # dynamic programming.
        # npp[i] := # number of partitions into palindromes for s[:i]
        # npp[0] # empty case
        # npp[i+1] # answer for full s

        # lesson: python string slicing can be tricky when we get to negative endings descending.

        npp = [ -1 for _ in range(len(s) + 1) ]
        # reflection: ran into issues making npp small. 
        # bc we want to depend on the case starting before char 0.
        npp[0] = 1 # only used to add to npp[:0]
        actualp = [[] for _ in npp ] # actual solutions
        actualp[0] = [[]]
        for i in range(1,len(s)+1):
            total = 0
            for j in range(i): 
                # for j = 0: we are checking if whole thing is a single palindrome,
                # and adding 1 if so. 
                suffix = s[j:i]
                if j == 0:
                    reflected = s[i-1::-1] # lesson: for descening indices to include 0, need to treat differently than ending at some point above 0 (- 1 will mess things up)
                else:
                    reflected = s[i-1:j-1:-1] # lesson: 

                #print(f"{npp=} comparison {j=} {i=} {suffix=} {reflected=}")
                if suffix == reflected: # slow check.
                    actualp[i].extend([p + [suffix] for p in actualp[j] ])
                    total += npp[j] # npp j includes jth car.
                
            # for i = len(s)+1
            # j ranges from 0 to len(s)
            # check s[0:len(s)+1] is a palindrome (whole string)
            # end case: check s[len(s):len(s)+1] is a palindrome. (last char case)
            npp[i] = total
            assert npp[i] == len(actualp[i])

        return actualp[-1]