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
        position_strings = [ '.'*k + 'Q' + '.'*(n-k-1)
            for k in range(n)
        ]

        placements = [] # all recovered ones. list of list of pairs

        # used to represent current board state 
        cols = [False for _ in range(n)] 
        # True for position [i] if that col i is occupied.
        diag1s = [False for _ in range(2*n-1)]
        # True for (row,col) if row - col is occupied somewhere
        diag2s = [False for _ in range(2*n-1)]
        # True for (row,col) if row + col is occupied.

        def dfs(row) -> list: # returns list of positions possible after here
            # propose a column position for row n - n_left:
            if row == n: # no positions possible anymore
                return [[None]] # indicates only end is possible

            accumulated = []
            for col in range(n):
                diag1 = row - col 
                # goes from -(n-1) to n-1.
                # python negative indexing makes it work. 
                diag2 = row + col
                if cols[col] or diag1s[diag1] or diag2s[diag2]: 
                    continue # inviable
                else:
                    cols[col] = True
                    diag1s[diag1] = True
                    diag2s[diag2] = True

                    possible = dfs(row+1)
                    for p in possible:
                        new_path = [(row,col)] + p
                        accumulated.append(new_path)

                    # clear state added before trying next option
                    cols[col] = False
                    diag1s[diag1] = False
                    diag2s[diag2] = False

            return accumulated



        all_solutions = dfs(0)
        def translate_soln(soln):
            output = []
            for pair in soln:
                if pair is None:
                    continue
                output.append(position_strings[pair[1]])
            return output

        return [translate_soln(sol) for sol in all_solutions]

        # complexity analysis:
        # space: at any given time only tracks the current placement,
        # plus accumulated solutions. 
        # O(n) in current state. 
        # How many possible solutions can be accumulated?  not sure.
        # lists of output orderings are bound by n!, no other obvious bound.
        # but clearly cannot be that many.
        # 
        # time: from row n, we call the routine on potentially
        # n positions for this row, on row n+1. This makes the time: T(n+1)= O(n*T(n)). so, T(n) is n^n? More like n! bc we are reducing cols by 1 at most.

        # things that can be done better in this solution:
        # no need for the state object. just pass the 3 pieces.
        # saves typing. even 4 pieces was ok. it turned out one wasn't needed.
        # we could have added more.

        # things i did right: the data structures for checking if a position is valid.
        # instead of loops over the existing pieces, just check for conflict directly.




        # notes on my approach to the problem:
        # identified approach early, after thinking about the problem a couple
        # of different ways.
        # tried to be clever initially, trying to solve nqueens in terms of smaller 
        # nqueens.
        # changed tack after just thinking i should just go row by row given
        # every row must have a queen placed within some column.
        # backtracking was necessary, i knew that. but first i wanted to understand
        # what checks were needed to figure out a position was ok. this was not bad, but may have taken some time. 
        # I wrote a loop, this was a bad idea, it took time and i knew it ultimately was not going to make backtracking easy for me,  I should have started with recursive approach from the get-go to simplify the thinking.

        # I went back and forth with what the structure would hold (free vs used positions, rows left vs current row). not sure this is necessary, causes code changes.
        # the base case was wrong initially. i returned empty.
        # this gave no signal on whether there was a valid placement or not.
        # when using the result from the recursive step, i could have foreseent this
        # if i had reasoned about the step before the last.
        # on the other hand, running the program revealed the problem and i fixed it, so not sure that's a big deal after all.








                

        