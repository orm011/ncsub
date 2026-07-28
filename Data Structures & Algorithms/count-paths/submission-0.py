import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1x1 grid: only one option: (0 + 0) C 0
        # 1x2 grid: only one option: (1 + 0) C 0
        # 2x2 grid: 2 options: (2-1 )
        return math.comb(n -1 + m - 1, n - 1)

        