class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #len of board = rowsa nd len of 1st list = no. of col
        row, col = len(board), len(board[0])
        #This stores cells we already used, to avoid visting to cells that are already visited
        path = set()

        def dfs(r, c, i):
            #If we matched all letters, then return true
            if i == len(word):
                return True
            #Conditions for out of bounds or Letter doesn’t match or Already used the cell
            if (r < 0 or c < 0 or r >= row or c >= col or word[i] != board[r][c] or (r, c) in path) :
                return False
            #Add current cell to visited list
            path.add((r, c))
            #Move down, up, right, left to check the letter
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            #Remove the cell so it can be reused in another path
            path.remove((r,c))
            #If any direction worked return true
            return res
        #Check every position as a starting point.
        for r in range(row):
            for c in range(col):
                #If word found anywhere, return True
                if dfs(r, c, 0): return True
        return False
        