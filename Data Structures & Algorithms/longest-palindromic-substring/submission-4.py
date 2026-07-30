# continuing solution 2 but this time not recursively.
# trouble case: long strings. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        lets consider a different framing
        s[0] may or may not be part of a longest palindrome subseq.
        if it is, then it is made up of the longest 
        sub-palindrome s[1:last] where last is another instance of s[0]
        and moreover, it needs to start at s[1], and end right before a char equal to s[0]
        we can restrict to s[1:-1] and then just check the last char is s[0]

        if s[0] is not, then we will find the right answer in s[1:]
        
        big lesson here: i misunderstood the problem, and solved it that way.
        the examples didnt disambiguiate this possible confusion, so not fully my fault.
        But need to clarify you understand the problem early sometimes?
        """
        # the space of subproblems is small, start and end range from 0 to len(s)
        sz = len(s)
        solutions = [[None for _ in range(sz+1)] for _ in range(sz+1)]
        bestleft_solutions = {} # (start, endwith) -> soln

        # problem: many more dimensions here... many possible char endings
        # excludes end
        def checkPalindrome(start: int, end:int) -> bool:
            ans = True
            for offset in range(end - start):
                # violation detected
                if s[start + offset] != s[end - 1 - offset]:
                    ans = False
                    break

                # redundant
                if start + offset > end - 1 - offset:
                    break
            return ans

        def bestLeft(start: int, end: int, endwith: str) -> [str]:
            """
            returns the longest palindrome starting at s[start:] ending before end
            for now implemented naively
            """
            if end == start: # empty subcase
                return [] # longest palindrome size 0
            elif end - start == 1: # single char is always a palindrome
                return [s[start]] if s[start] == endwith else []
            
            memoized = bestleft_solutions.get((start, endwith), None)
            if memoized:
                return memoized
    

            for right_index in range(end - 1, start - 1, -1):
                if s[right_index] == endwith:
                    if checkPalindrome(start, right_index):
                        break
            
            # if right_index == start # need to tell apart if that matched or not.
            if s[right_index] == endwith:
                best = [s[i] for i in range(start, right_index+1)]
            else:
                best = []

            bestleft_solutions[(start, endwith)] = best
            return best
        
        def recSolution(start: int, end: int) -> [str]: # s is implicit throughout
            if end == start: # empty subcase
                return [] # longest palindrome size 0
            elif end - start == 1: # single char is always a palindrome
                return [s[start]] 

            if solutions[start][end] is not None:
                return solutions[start][end]

            # find the best palindrome including the first char
            first_char = s[start]
            
            # find the longest left-palindrome within start+1:end - 1
            # notice that if there are multiple palindromes we should pick the
            # left most one
            longest_sub_type1 = [first_char] + bestLeft(start+1, end, first_char)

            if len(longest_sub_type1) == end - start:
                longest_sub_type2 = [] # ignore
            else:
                longest_sub_type2 = recSolution(start+1, end)

            if len(longest_sub_type1) >= len(longest_sub_type2):
                ans = longest_sub_type1
            else:
                ans = longest_sub_type2

            # memoize
            solutions[start][end] = ans
            return ans
            
        chars = recSolution(0, len(s))
        assert chars[::-1] == chars, "not symmetric"
        # problem: substring is more constrained than subsequence.
        # seems correct, but runtime: seems to become O(N^3) thanks to checkPalindrome
        # within BestLeft
        # might as well do a check palindrome on all possible locations.
        # we see a recursion tree for best left... 

        return ''.join(chars)        