class Solution:
    def isHappy(self, n: int) -> bool:
        # if a number cycles through, 
        # it could take a long time, demaning space 
        # proprotional to cycle time to check for duplicates
        # using a set  structure.
        # will instead do a fast&slow pointers approach
        def step(n: int) -> int:
            total = 0
            while n > 0:
                n,rem = divmod(n,10)
                total += rem**2
            return total
            
        fast = step(n)
        slow = n
        while fast != slow and fast != 1:
            slow = step(slow)
            fast = step(fast)
            if fast == 1 or fast == slow:
                break
            fast = step(fast)

        return fast == 1 # otherwise cycle detected

        # analysis:
        # time
        # an trasient of size k followed by cycles of size c.
        # vs transient of size k followed by 1.
        # fast and slow will match within k + c iterations.
        # why? slow and fast are both within the cycle by 
        # iteration k.
        # at that point, it will take at most one full cycle traversal of fast to overtake.
        # O(k + c/2) time.
        # if it becomes 1: k/2. 
        # O(k+c) where c = 1 if number is 1. 
        # O(1) space        


        