class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        totals = []
        operators = ['-', '+', '*', '/']
        for t in tokens:
            #print(f"{t=} {totals=}")
            if t not in operators:
                totals.append(int(t))
            else:
                op = t
                arg2 = totals.pop()
                arg1 = totals.pop()
                if op == '+':
                    newtotal = arg1 + arg2
                elif op == '-':
                    newtotal = arg1 - arg2 
                elif op == '*':
                    newtotal = arg1 * arg2 
                else:# op == '/':
                    absarg1 = abs(arg1)
                    absarg2 = abs(arg2)
                    absdiv = absarg1 // absarg2
                    if (arg1 < 0 and arg2 > 0) or (arg1 > 0 and arg2 < 0):
                        newtotal = -absdiv
                    else:
                        newtotal = absdiv
                    
                totals.append(newtotal)
        #print(f"after {t=} {totals=}")
        return totals[0]
            


        