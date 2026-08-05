import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # only doable if
        # capacity >= carry[i] for all i. where carry is the amount that must
        # be carried. carry[i] is the sum of numPassengers[j] where j<=i minus
        # the sum of numPassengers[k] where k <= i and to[k] <= i
        # lets sort trips by from[] field. 
        trips.sort(key=lambda trip: trip[1])
        current = 0 # current number of passengers in car.
        # idea: go along the trips list in "from" order.
        # drop all passengers that needed to be dropped before or at this station.
        # add passengers as specified on each step.
        # if current crosses capacity, it cannot be done.

        pending_tos = [] # we will use a heap since we need to only drop off the 
        # earliest toi destinations
        for i in range(len(trips)):
            numPi, fromi, toi = trips[i]

            while pending_tos and pending_tos[0][0] <= fromi:
                (drop_toi, count) = heapq.heappop(pending_tos)
                current -= count
                assert drop_toi <= toi

            if current + numPi > capacity:
                return False

            # add to drop off schedule
            heapq.heappush(pending_tos, (toi, numPi))
            current += numPi

        
        return True


        