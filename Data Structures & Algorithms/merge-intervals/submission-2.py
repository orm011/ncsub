class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge all overlapping intervals only
        # constraint: start, end <= 1000
        # bc of constraint:
        # one possible approach:
        # mark start with 1, end with -1, 
        # then start interval when going from 0->1 (or more)   # and end interval when going back to 0. 
        countstarts = [0 for _ in range(1001)]
        countends = [0 for _ in range(1001)]
        maxend = 0
        for start, end in intervals:
            countstarts[start] += 1
            countends[end] += 1
            # handles [0,1][1,2] bc cancel out
            maxend = max(maxend, end)
        
        cumsum = 0
        output = []
        # handling [0,0] one element interval
        # need to distinguish +1 -1 from 0, add second 
        # structure

        for i in range(maxend+1):
            prev = cumsum
            cumsum += countstarts[i]
            if prev == 0 and cumsum > 0:
                # found start
                output.append([i])
                prev = cumsum
            
            cumsum -= countends[i]
            if  prev > 0 and cumsum == 0:
                # found end
                output[-1].append(i) 

            # when one interval ends and another starts,
            # we first increment starts, making ct 2
            # and prev is not 0, so interval started
            # then we remove the other, staying at 1
            # and we also do not need to append end.

            # but, when we deal with one elt interval.
            # start applies first, we add it, then end.
            # also add it. which is desirable.  
        return output

        # complexity: 
        # Space: O(1000) + O(input) due to constraint
        # and output respectively.
        # Time: we iterate through input once O(n)
        # then iterate through fixed size array O(1)
        # both O(n)



        