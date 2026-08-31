class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # get all possible mappings of digits to letters.
        results = []
        # challenge, there are many solutions for every char,
        # answer will blow up as length increases.
        # we will traverse the space of choices recursively 
        # while tracking the choices of higher levels via the path var. 
        path = []
        n = len(digits)

        num2letters = ['', '', 'abc', 'def', 
                        'ghi', 'jkl','mno', 
                        'pqrs', 'tuv', 'wxyz']

        if n == 0:
            return results
            
        def gensol(i: int) -> None:
            if i == n:
                results.append("".join(path)) # all choices made
                return
            
            digit = int(digits[i])
            options = num2letters[digit]
            for o in options:
                path.append(o)
                gensol(i+1)
                path.pop() # backtrack on this choice

        gensol(0)
        return results
        