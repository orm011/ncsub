class CountSquares:

    def __init__(self):
        # representation?
        self.points = {} # map point -> count
        self.byx = {} # map x -> set of points
        self.byy = {} # map y -> set of points

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 1
        else:
            self.points[point] += 1

        (x,y) = point
        if x not in self.byx:
            self.byx[x] = {point}
        else:
            self.byx[x].add(point)
        
        if y not in self.byy:
            self.byy[y] = {point}
        else:
            self.byy[y].add(point)
        
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
        aligned_x = self.byx.get(x, set({})) # list of points aligned vertically.
        # print(f"{point=} {aligned_x=}")
        heights = {}
        for point in aligned_x:
            count = self.points[point]
            (_, y1) = point
            height = abs(y1 - y)
            if height == 0: # identical point to query.
                continue
            
            curr = heights.get(height, set({}))
            curr.add(point)
            heights[height] = curr

        aligned_y = self.byy.get(y, set({})) # points aligned horizontally.        
        widths = {}
        for point in aligned_y:
            # build the widths structure.
            (x1,_) = point
            width = abs(x1 - x)
            if width == 0:
                continue

            curr = widths.get(width, set({}))
            curr.add(point)
            widths[width] = curr
            
        total = 0
        for width,aligned_points in widths.items():
            distance_matches = heights.get(width, set({}))
            # nested loop is at most size 4
            for (x1,y1) in aligned_points:
                c1 = self.points[(x1,y1)]
                for (x2,y2) in distance_matches:
                    c2 = self.points[(x2,y2)]
                    x3 = x if x1 == x2 else x1 if x2 == x else x2
                    y3 = y if y1 == y2 else y1 if y2 == y else y2
                    c3 = self.points.get((x3,y3), 0)
                    total_options = c1*c2*c3
                    if total_options:
                        total += total_options
            
        return total


    # bugs found:
    # copy paste error when adding.
    # the case of a query duplicating a point. yielded distance 0.
    # and then sinced that point is aligned in both x, and y, it matches.
    # analysis. add(): O(1) update three hash data structures.
    # count(): 
        # query initial hash
        # build height hash: potentially O(n) if all points are aligned vertically.
        # join horizontal to vertical alignment. 
        #   (hash join) iterate through horizontal alignment, check if 
        # any matches. if something does match, 
        # then check if fourth point in there.
        # can we really save anything here.
        # the vertical case answer is 0, ie very few possible matches.
        # we could check if horizontal has fewer matches than vertical
        # we could keep the x values and y values sorted. 
        # this would increase the add time. 
        # but then we can query ranges to discard points that would not match.
