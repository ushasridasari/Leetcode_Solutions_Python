class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Stores the number of rows and columns of the board.
        rows, cols = len(board), len(board[0])
        #Creates a helper function to explore connected "O" cells.
        def Capture(r, c):
            #If out of bounds or cell is not 'O', return.
            if ( r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"):
                return
            #Marks the current "O" as safe.
            board[r][c] = "T"
            #Moves down, up, right, left
            Capture(r + 1, c)
            Capture(r - 1, c)
            Capture(r, c + 1)
            Capture(r, c - 1)
        #Checks the left edge and right edge
        for r in range(rows):
            if board[r][0] == "O":
                Capture(r, 0)
            if board[r][cols - 1] == "O":
                Capture(r, cols - 1)
        ##Checks the top border and bottom border
        for c in range(cols):
            if board[0][c] == "O":
                Capture(0, c)
            if board[rows - 1][c] == "O":
                Capture(rows - 1, c)
        #Loops through each cell
        for r in range(rows):
            for c in range(cols):
                #If cells "O" are trapped and convert them into "X"
                if board[r][c] == "O":
                    board[r][c] = "X"
                ##If cells "T" are trapped and convert them into "0"
                elif board[r][c] == "T":
                    board[r][c] = "O"

#TC: O(m*n)
#SC: O(m*n)

        
        