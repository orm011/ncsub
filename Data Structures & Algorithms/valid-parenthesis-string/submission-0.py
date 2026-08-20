class Solution:
    def checkValidString(self, s: str) -> bool:
        # lets think dynamic recursively.
        # chars 0:k+1 are a valid sequence if and only if
        # there is an assignment to * so the sum is greater than or equal
        # to 0 at every point, and the final count is 0.
        # consider how to get 0:k+2 add to 0, while keeping every prefix geq 0.
        # char k+1 could be '(': in which case its impossible to be 0 while 
        # prefix being geq0.
        # ')' in which case we need the prefix :k+1 to stay postive and have sum 1.
        # '*': in which case we need the prefix to either sum to 1 (use as ')), or sum to 0 (remove)
        # more generally for :k+2 to add up to h, if the symbol is ')', then 
        # we need the prevoius sum should be h+1.
        # if the symbol is '(', then the previous sum should be h-1.
        # if the symbol is '*', then the have three subcases.
        # each '*' extends the range of future sums by +1, -1, or none.
        
        upper = 0
        lower = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == '(':
                upper += 1
                lower += 1
            elif c == ')':
                if upper > 0:
                    upper -= 1
                    lower = max(0, lower - 1)
                else:
                    return False # no possible way
            else: # could go two ways
                upper += 1
                if lower > 0: # cannot make it lower than 0.
                    lower -= 1
        
        # note every possibility in between lower and upper is possible:
        # its true for the first star,
        # for the second star: add 2 corresponds to tow both '('
        # add 1 to single '('

        return lower == 0



        