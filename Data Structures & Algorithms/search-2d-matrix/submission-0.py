import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # basic idea: binary search on full array (base)
        # however, original structure does not follow array shape.
        # we can implement binary search translating an index into a position.
        # that would be log(m*n).
        # alternatively, can use existing binary search tools.
        # first find the right row (m numbers), then the right position within a row.
        # (n). also gives you log m + log n.

        # bisect on the first element of each row.
        # rows at idx or later will be greater than the element.
        # the row we care is the one before it.   
        rowidxafter = bisect.bisect_right(matrix, x=target, key=lambda x : x[0])
        if rowidxafter == 0:
            return False
        
        rowidx = rowidxafter - 1
        pos = bisect.bisect_left(matrix[rowidx], x=target)
        if pos == n:
            return False

        return matrix[rowidx][pos] == target



        