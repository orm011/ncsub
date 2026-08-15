class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i] # of days j > i to wait before temp[j] > temp[i]
        # eg. eg, if augmenting every day: 1 everywhere. 0 at least.
        #   if you descend and then climb, answers decreased by one for each.
        # result[i] depends on having seen everything after.
        # result[i-1] = 0  always
        # going backward from last to first,
        # when we see a bigger temperature, no other temperature
        # afterward needs to be remembered.
        # however, smaller temperatures may still matter because 
        # they affect the day count. 
        # for number in position [i], whats the next higher day.
        # naive approach: loop until find next. O(n)
        # redundant work: that next value could also be the best
        # value for a lot of entries before and after.
        
        # result[i] = 1 if result[i+1] > result[i] else result[i+1] + 1
        # recusion is wrong actually.
        argmaxtemps = [] 
        n = len(temperatures)
        # descending positions of non-dominated temps at the moment.
        # a temp[i] is dominated by temp[j] if temp[j] > temp[i] and j < i 
        results = [0] * n 
        for i in range(n - 1, -1, -1):
            while argmaxtemps and temperatures[i] >= temperatures[argmaxtemps[-1]]:
                argmaxtemps.pop()
            # now we know either argmaxtemps is [] (nothing seen after was bigger)
            # or the last temperature in it is greater than to current temp
            # that last temperature is also the closest index, since we append
            if argmaxtemps:
                results[i] = argmaxtemps[-1] - i
            # nothing after is bigger
            argmaxtemps.append(i) # next temp sees this one.

        # working space: O(n) potentially for argmaxtemps
        # result space: O(n)
        # working time: each input element gets added once, and poppoed at most once
        # so O(n)
        return results




            