class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # a legal expression of n+1 pairs
        # can take a few forms, assuming we have an n-pair expr
        # ( expr )
        # expr ()
        # ex (pr) 
        # it must take one of these.
        # want to avoid repetition though... if possible.
        # however expr() and ()expr may generate with redundancy.
        # any other way? eg right most paren. where does it match paren
        # show up?  expr () or  ex ( pr ). If we do express it this way
        # it may be unique
        # () -> 
        # ()() or (()) ->
        # ()()(). (())()
        # ()(()). ((()))
        # (()()).
        # approach 1: first approach with a set and test. 
        # exponential growth (catalan numbers) + some redundancy. 
        # 2n Choose n / (n+1)

        # actually initial attempt was wrong. those are not the only ways
        # to generate parens. 

        # next attempt: what are we missing here. 
        # expr -> Nil
        # expr -> expr ( expr ) # this summarizes all possibilities.

        previous = [""]
        result = []
        for _ in range(1,n+1):
            for expr in previous:
                # find all split points
                count = 0
                for i,c in enumerate(expr):
                    if count == 0:
                        result.append(f"{expr[:i+1]}({expr[i+1:]})")
                    
                    if c == '(':
                        count += 1
                    else:
                        count -= 1

                # append the end one
                result.append(f"{expr}()")
            
            previous = result
            result = []

#        print(f"{ex1 - ex2=} {ex2 - ex1=}")
        return previous



            



        