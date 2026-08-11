class Solution:
    def reverse(self, x: int) -> int:
        # reverse digits of an integer
        # option 1: convert to string and reverse string, check if string
        # is outside signed int32 range. (note they say not to use any
        # representation outside the range)
        # space & time: log(x) chars in the value of x.
        # alternatively, can get the most significant / least significant
        # digit and work one of those at a time.
        # space O(1). time: log10(x) if we extract digit by digit.
        ans = 0
        sign = -1 if x < 0 else 1 
        x = sign*x # NB: this breaks for -2^31

        # 32 bit = 8* F. 31 bit is 8 then 7*F 
        max_int = 0x07FFFFFFF # note is odd so not divisible by 10.        
        max_factor = max_int // 10
        max_rem = max_int % 10
        check = False
        while x > 0:
            digit = x % 10
            x = x // 10 # next one
            if ans < max_factor or (ans == max_factor and digit <= max_rem):
                ans = ans*10 + digit # guaranteed to not exceed max int.
                # print(f"{hex(ans)=}")
            else:
                return 0


            # elif sign < 0 and (ans == max_factor and digit == max_rem + 1
            #     and x == 0): # x after decreasing, compute negative case
            #     return -10*ans - digit
            # else: # every remaining negative case is not repr.
            #     return 0

        # what changes if x is negative.
        # x// 10 is rounded toward the negative side. 
        # eg. -1//10 is not 0, but -1. rem then is 9
        # -1*10 + 9 = -1
        # if we simply treat it as positive:
        # the max value is too aggressive, but this only matters at the last 
        # check
        
        # problem: converting to positive only works for numbers in range.
        # handle that case separately
        # this will be incorrect for some boundary case negatives.
        ans = sign*ans
        # print(f"{hex(ans)=}") 
        return ans


    


            

        