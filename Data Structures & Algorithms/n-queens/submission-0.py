class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ### solution for 1 queen: ok
        ## solution for 2 queens: 0
        ## solution for 3 queens: 0 (can do 2 in 3x3)
        ## solution for 4 queens: 2
        ## solution for 5 queens in grid of 5.

        ## some intuition. to show there are no more arrangements for 4 queens.
        ## subset of queens that fits within a 3 x 3 grid must be a solution
        ## for the smaller 3x3 grid problem.

        ## alternative: try a position for the first row.
        ## then one for the second row from the remaining columns.
        ## then one for the third row.. etc. backtrack there is a diagonal 
        ## violation.
        # for 3 x 3: 4 + 1
        # for 4 x 4: 6 + 1 checks out.
        # for 2 x 2: 2 + 1. good. 

        # diagional k made up of values with r - c = k.
        # eg 0,0, 1,1, 2,2.
        # 1,0  2,1, 3,2

        # diagtype2 k made up of values with r + c = k.
        # eg 0,3 1,2 2,1 3,0:
        # idea, start by building up some positions,
        # when no move is possible, if there no solution,
        # backtrack by returning to caller. which can resume trying a different move. 
        board_state = {'positions':[],
                'cols': set(),
                'diag1': set(), # r - c
                'diag2': set() # r + c
            }

        placements = [] # all recovered ones. list of list of pairs

        def dfs(state, row) -> list: # returns list of positions possible after here
            # propose a column position for row n - n_left:
            if row == n: # no positions possible anymore
                return [[None]] # indicates only end is possible

            accumulated = []
            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                if col in state['cols'] or diag1 in state['diag1'] or diag2 in  state['diag2']:
                    continue # on to next
                else:
                    state['cols'].add(col)
                    state['diag1'].add(diag1)
                    state['diag2'].add(diag2)

                    possible = dfs(state, row+1)
                    for p in possible:
                        new_path = [(row,col)] + p
                        accumulated.append(new_path)

                    # clear state added before trying next option
                    state['cols'].remove(col)
                    state['diag1'].remove(diag1)
                    state['diag2'].remove(diag2)

            return accumulated

        all_solutions = dfs(board_state,  0)
        def translate_soln(soln):
            output = []
            for pair in soln:
                if pair is None:
                    continue
                col = pair[1]
                base_str = ['.' for _ in range(n)]
                base_str[col] = 'Q'
                output.append(''.join(base_str))
            return output


        return [translate_soln(sol) for sol in all_solutions]



                

        