class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we need to find if there is a path in the board matching
        # the word.
        # the word can be seen as a path strating from the initial word
        # with a specific kind of condition.
        # initial approach:
        # find all locations in the board with the initial letter.
        # these are the only possible starting points. 
        # for each of them do a DFS where you explore only those directions
        # that match the next condition in your word.
        # you need to ensure to come back to previous candidates.
        # can be done via backtracking (explore solution, undo invalid steps)
        # each level need to access state from the current path to 
        # avoid revisting cells already in progress.

        m = len(board)
        n = len(board[0])
        w = len(word)

        # marks if something is seen so far, also, sentinels on the edge
        isvalid = [[False if i in (0,n+1) or j in (0,m+1) else True  for i in range(n+2)] for j in range(m+2)]
        #print(f"{isvalid=}")
        def backtrack(i, j, k): 
            # k is position in the word to match
            # ij is which position of the board we're at.
            if board[i][j] == word[k] and k == w - 1: # end of word
                return True

            #print(f"{i=}{j=}")
            if board[i][j] != word[k]:
                return False

            isvalid[i+1][j+1] = False # in current path
            
            if isvalid[i-1+1][j+1] and backtrack(i-1, j, k + 1):
                return True
            if isvalid[i+1][j-1+1] and backtrack(i, j-1, k + 1):
                return True
            if isvalid[i+1+1][j+1] and backtrack(i+1, j, k + 1):
                return True
            if isvalid[i+1][j+1+1] and backtrack(i, j+1, k + 1):
                return True

            isvalid[i+1][j+1] = True
            return False
            

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True

        return False








        





                    
