class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # intuitions:
        # 1. recursive pattern: once we peel off top and right, 
        # bottom left, the remaining core follows the same pattern 
        # as problem of size n - 2. 

        # 2. formula: starts with i = 0, j=0 then j = -1 fixed.. then i = -1
        # then j = 0. then i = 1, j=1

        output = []
        height = len(matrix)
        width = len(matrix[0])

        h,remh = divmod(height, 2)
        w,remw = divmod(width,2)

        def rec(k: int): # starting at top left corner i=k,j=k
            # base cases: 1x1 and 2x2. (3x3 reduces to 1x1)
            # given n, how do we know we are in the 1x1 case.
            # if n = 2h + 1 is odd: then when k = h, we are in the middle.
            # if n = 2h, then when k = h - 1, there is a 
            # 2x2 matrix at that point: verify h - 1 + h - 1 + 2 = 2h.
            remainingh = height - 2*k
            remainingw = width - 2*k
            
            # basecases
            if remainingh == 0 or remainingw == 0:
                return # nothing to do
            elif remainingh == 1:
                for i in range(k,width - k):
                    output.append(matrix[k][i])
            elif remainingw == 1:
                for i in range(k, height-k):
                    output.append(matrix[i][k])
            # else, at least 2x2
            else:
                top = [[k,i] for i in range(k, width-k-1)] # skip right most
                for i,j in top:
                    output.append(matrix[i][j])

                right = [[i, width - k - 1] for i in range(k,height-k-1)] # top to bottom
                for i,j in right:
                    output.append(matrix[i][j])

                
                bottom = [[height - k - 1, width - i - 1] for i in range(k,width-k-1)] # right to left
                for i, j in bottom:
                    output.append(matrix[i][j])

                left = [[height - i - 1, k] for i in range(k,height-k-1)] # bottom to up
                # when k = 0. -i 
                for i,j in left:
                    output.append(matrix[i][j])

                rec(k+1)

        rec(0)
        return output                



            
        