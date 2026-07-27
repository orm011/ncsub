import heapq

# def print(*args, **varargs):
#     pass

class MedianFinder:

    def __init__(self):
        self.median = None
        self.below_median = []
        self.above_median = []
        # as we add new elements, we preserve the invariant that len below_median == above_median
        # setting the median to None in the even case.
        # invariants self.below_median[0] <= self.median <= self.above_median[0]
        # len(self.below_median) == len(self.above_median)

    def __str__(self):
        return f"{self.below_median, self.median, self.above_median}"

    def __repr__(self):
        return str(self)

    def addNum(self, num: int) -> None:
        # print(f"addNum: {num=} {self=}")
        current = self.findMedian()
        if current is None: # empty case
            self.median = num
        elif num <= current:
            heapq.heappush_max(self.below_median, num)
        elif num > current:
            heapq.heappush(self.above_median, num)
        else:
            pass

        # now rebalance
        if len(self.below_median) > len(self.above_median):
            if self.median is not None: # if we have a median set. just move that
                heapq.heappush(self.above_median, self.median)
                self.median = None
            else:
                new_median = heapq.heappop_max(self.below_median)
                self.median = new_median

        elif len(self.below_median) < len(self.above_median):
            if self.median is not None:
                heapq.heappush_max(self.below_median, self.median)
                self.median = None
            else:
                new_median = heapq.heappop(self.above_median)
                self.median = new_median

        else:
            pass


    def findMedian(self) -> float:
        if self.median is not None:
            return self.median
        elif self.below_median: # must have at least 2
            return (self.below_median[0] + self.above_median[0])/2
        else:
            None # empty case
        
        