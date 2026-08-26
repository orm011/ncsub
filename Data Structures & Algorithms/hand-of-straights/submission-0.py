from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sorting initially seems wise, will reveal all possibilities.
        # if there is any jump, then we know this is not possible.
        # however it could be that there is only a jump once we have used up
        # some cards.
        # note every card has to be used up, so can do this recursively.
        hand.sort()
        # insertion order is sorted order
        counts = Counter(hand)
        # we will remove runs from counts until we empty it.
        while counts:
            minx = next(iter(counts))
            for k in range(minx, minx + groupSize):
                if counts[k] > 0:
                    counts[k] -= 1
                    if counts[k] == 0:
                        del counts[k]
                else:
                    return False # missing

        return True
