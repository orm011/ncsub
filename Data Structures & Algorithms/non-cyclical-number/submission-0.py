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
            if fast == 1:
                break
            fast = step(fast)

        return fast == 1 # otherwise cycle detected

        # 


        