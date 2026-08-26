class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = [0]*(max(hand) + 1)
        for num in hand:
            counts[num] += 1

        i = 0
        runlen = 0
        resume = None # memory of where to restart once current run is over.
        while i < len(counts):
           # print(f"{i=} {runlen=} {resume=} {counts[:10]=}")
            if counts[i] == 0 and runlen == 0: # skip position
                i += 1
                continue
            elif counts[i] == 0 and runlen > 0: # ongoing run broken
                return False # broke a run
            elif counts[i] > 0: # may start run or increase one or complete
                counts[i] -= 1
                runlen += 1

                if counts[i] > 0 and resume is None:
                    resume = i # checkpoint

                # by default move forward one
                i += 1

                # but check if run completed
                if runlen == groupSize:
                    runlen = 0 # reset run
                    if resume is not None:
                        i = resume # jump to resume point
                        resume = None
            
        return runlen == 0

            

            