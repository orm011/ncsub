
OUTSIDE = (-1,-1)

class UnionFind:
    def __init__(self, n, m):
        self.parent = {OUTSIDE:OUTSIDE}
        self.size = {OUTSIDE:1}
    
    def find(self, a) -> int:
        curr = a
        path = [curr]
        while True:
            ret = self.parent.get(curr, None)
            if ret is None or ret == curr:
                ans = ret
                break
            else:
                curr = ret # traverse parent
                path.append(curr)
        
        # compression
        if ans is not None:
            for c in path:
                self.parent[c] = ans

        return ans
    

    def union(self, a, b) -> int:
        ra = self.find(a)
        rb = self.find(b)
        if (ra,rb) == (None, None):
            self.parent[b] = b # self root
            self.parent[a] = b
            self.size[b] = 1 if a == b else 2
        elif ra == None:
            self.parent[a] = rb
            self.size[rb] += 1
        elif rb == None:
            self.parent[b] = ra
            self.size[ra] += 1
        elif ra == rb:
            return 
        else: 
            if ra == OUTSIDE or rb == OUTSIDE:
                self.parent[rb] = OUTSIDE
                self.parent[ra] = OUTSIDE
                self.size[OUTSIDE] = self.size[rb] + self.size[ra]
            else:
                if self.size[ra] < self.size[rb]:
                    ra, rb = rb, ra

                self.parent[rb] = ra # smaller nested in larger
                self.size[ra] += self.size[rb]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0]) # len > 0 guaranteed

        X = 'X'
        O = 'O'

        components = UnionFind(n, m)

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == O:
                    components.union((i,j), OUTSIDE)

        for j in [0, n - 1]:
            for i in range(m):
                if board[i][j] == O:
                    components.union((i,j), OUTSIDE)

        for i in range(m):
            for j in range(n):
                if board[i][j] == O:
                    up = board[i - 1][j] if 0 <= i - 1 else None
                    left = board[i][j - 1] if 0 <= j - 1 else None
                    
                    if up == O:
                        components.union((i,j),(i-1,j))
                    if left == O:
                        components.union((i,j), (i, j-1))
                # can worry about left and up. bottom and right are symmetric.
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == O:
                    comp = components.find((i,j))
                    if comp is None or comp != OUTSIDE:
                        board[i][j] = X

        # in place remove all the surrounded regions
        # approach: build up a union-find structure 
        # O(m*n) space for structure
        # and time to build up for entries
        # last loop: O(m*n log m*n)



        