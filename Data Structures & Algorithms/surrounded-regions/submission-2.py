class UnionFind:
    def __init__(self, n, m):
        self.parent = {}
        self.n = n
        self.m = m
    
    def isboundary(self, k):
        (i,j) = divmod(k, self.n)
        m = self.m
        n = self.n
        return  i == 0 or i == m - 1 or j == 0 or j == n - 1 

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
        elif ra == None:
            self.parent[a] = rb
        elif rb == None:
            self.parent[b] = ra
        else:
            if self.isboundary(ra):
                self.parent[rb] = self.parent[ra]
            else:
                self.parent[ra] = self.parent[rb]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0]) # len > 0 guaranteed

        X = 'X'
        O = 'O'

        def tonum(i,j):
            return i * n + j

        def isboundary(k):
            (i,j) = divmod(k,n)
            return  i == 0 or i == m - 1 or j == 0 or j == n - 1 
        
        components = UnionFind(n, m)

        for i in [0, m - 1]:
            for j in range(n):
                k = i * n + j
                if board[i][j] == O:
                    components.union(k,k)

        for j in [0, n - 1]:
            for i in range(m):
                k = i * n + j
                if board[i][j] == O:
                    components.union(k,k)

        for i in range(m):
            for j in range(n):
                k = tonum(i, j)
                if board[i][j] == O:
                    up = board[i - 1][j] if 0 <= i - 1 else None
                    left = board[i][j - 1] if 0 <= j - 1 else None
                
                    if up == O:
                        h = tonum(i - 1, j)
                        components.union(k,h)
                    if left == O:
                        h = tonum(i, j - 1)
                        components.union(k,h)
                # can worry about left and up. bottom and right are symmetric.
        
        for i in range(m):
            for j in range(n):
                k = tonum(i,j)
                if board[i][j] == O:
                    comp = components.find(k)
                    # print(f"{k=} {comp=}")
                    if comp is None or not isboundary(comp):
                        board[i][j] = X 


                








        # in place remove all the surrounded regions
        # approach: build up a union-find structure 
        # O(m*n) space and time to build up for entries




        