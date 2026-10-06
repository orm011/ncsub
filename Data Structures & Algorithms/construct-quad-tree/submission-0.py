"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # check values on part.
        # if all equal: it is a leaf
        # split into four if not a leaf, repeat.
        # each time need to check different sections: repeated scanning
        # of the whole matrix in the worst case (imagine checkerboard)
        # idea: cumulative sum so that we can tell change by looking
        # at start and end ranges.

        # idea: horizonal cumulative sum.
        # then vertical cumulative sum of the above. (h,h) (k,k): 
        # can compare sums at both and if delta is 0, we are safe.

        n = len(grid)

        grid = [[x for x in row] for row in grid] # copy it
        # grid[i][j] means all the 1's between 0,0 and i,j included.
        # at most can be i+1*j+1
        # can compute via: first left to right arr[i][j] has cumulative sum
        # now row 

        for i,row in enumerate(grid):
            for j,entry in enumerate(row):
                top = grid[i-1][j] if i-1 >= 0 else 0
                left = grid[i][j-1] if j-1 >=0 else 0  
                topleft = grid[i-1][j-1] if (j-1 >= 0 and i -1 >= 0) else 0
                grid[i][j] = grid[i][j] + top + left - topleft


        def get_label(i1,j1, i2,j2)-> int | None:
            # range is inclusive
            topleft = grid[i1-1][j1-1] if ((i1 - 1 >= 0) and (j1 - 1 >= 0)) else 0 

            left = grid[i2][j1 - 1] if j1 -1 >= 0 else 0
            top = grid[i1 - 1][j2] if i1 - 1 >= 0 else 0

            delta = grid[i2][j2] - left - top + topleft
            ones = (i2 - i1 + 1) * (j2 - j1 + 1) # 1 x 1 case: 1

            if delta == 0:
                ans =  0
            elif delta == ones:
                ans =  1
            else:
                ans =  None

           # print(f"label {i1=} {j1=} {i2=} {j2=} {delta=} {ans=}")
            return ans


        def build(i1, j1, i2, j2) -> 'Node': 
            label = get_label(i1, j1, i2, j2)
            if label is not None:
                return Node(val=label, isLeaf=True)
            # elif depth > 0:
            #     return None
            # mixed            
            ans = Node(val=0, isLeaf=False)
            midi = (i1 + i2) // 2 # can be equal to i1. 
            midj = (j1 + j2) // 2 # can be equal to j1.
            # 0 + 1 // 2 = 0
            # i1 mid1 0,0
            # midi+1, i2: 1,1

            ans.topLeft = build(i1,j1,  midi, midj)

            ans.topRight = build(i1, midj + 1, midi, j2)

            ans.bottomRight = build(midi+1, midj+1, i2, j2)
            ans.bottomLeft = build(midi+1, j1, i2, midj)

            return ans

        #print(f"{grid=}")
        return build(0,0,n-1,n-1)
