class CountSquares:

    def __init__(self):
        # representation?
        self.points = {}
        self.byx = {}
        self.byy = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 1
        else:
            self.points[point] += 1

        (x,y) = point
        if x not in self.byx:
            self.byx[x] = [point]
        else:
            self.byx[x].append(point)
        
        if y not in self.byy:
            self.byy[y] = [point]
        else:
            self.byy[y].append(point)

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        # given an [x,y], the only possible squares
        # are formed by  other points [x',y'] where
        # either x' = x or y' = y. that narrows down which 
        # are possible points we can use, and we can respond 0 already sometimes.
        # however, given this set of points, how do we know a square 
        # can be formed?
        # for a with w
        # [x, y] we need [x - w, y] or [x + w, y]
        # and [x, y + w] or [x, y - w]
        # and finally, given three points, there is only one possible fourth.
        # for each candiate second point, we have a width. 
        # then we need to check for existance of a third point, and a fourth point.
        # naive approach 1: consider all sets of three points  and check of square. (many combinations make this O(n^3))
        # navie approach 2: consider the possible neighbors. within that set

        x, y = point
        aligned_x = self.byx.get(x, []) # list of points aligned vertically.
        print(f"{point=} {aligned_x=}")
        heights = {}
        for (xprime,yprime) in aligned_x:
            height = abs(yprime - y)
            curr = heights.get(height, [])
            if height > 0:
                curr.append([xprime, yprime])
            heights[height] = curr

        aligned_y = self.byy.get(y, []) # points aligned horizontally.

        # insight: any height-width match fully determines a square
        print(f"{heights=}")
        total = 0
        for (xprime, yprime) in aligned_y:
            width = abs(xprime  - x)
            possible = heights.get(width, [])
            print(f"{possible=}")
            for (xsec, ysec) in possible:
                # fourth point must be:
                xthird = x if xprime == xsec else xprime if xsec == x else xsec
                ythird = y if yprime == ysec else yprime if ysec == y else ysec

                c = self.points.get((xthird,ythird), 0)
                total += c

        return total


