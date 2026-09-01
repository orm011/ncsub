class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        # matrix[i][j], i iterates over m, j over n
        output = [[ matrix[i][j] for i in range(m)] for j in range(n)]
        # output has height n, width m
        return output
        