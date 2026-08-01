class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = 0
        open_brackets = 0
        open_braces = 0

        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif ch == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False # mismatched symbol


        return stack == [] # all elements must have been matched by the end
        # some edge case: {[}]. will pass. This technique works for single symbol, fails for two.
        