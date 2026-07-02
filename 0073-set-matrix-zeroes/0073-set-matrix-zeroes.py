class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #number of rows and number of cols
        ROWS, COLS = len(matrix), len(matrix[0])
        #Creates a variable to remember if the first row contains a zero.
        rowZero = False

        #Loops through every row and col in the matrix.
        for r in range(ROWS):
            for c in range(COLS):
                #Checks if the current element is zero.
                if matrix[r][c] == 0:
                    #Marks the column by placing a zero in the first row.
                    matrix[0][c] = 0
                    #Checks if the zero is not in the first row.
                    if r > 0:
                        #Marks the row by placing a zero in the first column.
                        matrix[r][0] = 0
                    #Runs if the zero is in the first row.
                    else:
                        #Remembers that the first row should be turned into zeros later.
                        rowZero = True
        #Starts checking rows from the second row onward.
        for r in range(1, ROWS):
            #Starts checking columns from the second column onward.
            for c in range(1, COLS):
                #Checks if the current row or column was marked.
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    #Changes the current element to zero.
                    matrix[r][c] = 0

        #Checks if the first column needs to become all zeros.
        if matrix[0][0] == 0:
            #Loops through every row in the first column.
            for r in range(ROWS):
                #Makes every element in the first column zero.
                matrix[r][0] = 0

        #Checks if the first row originally contained a zero.
        if rowZero:
            #Loops through every column in the first row.
            for c in range(COLS):
                #Makes every element in the first row zero.
                matrix[0][c] = 0

    #TC: O(m*n)
    #SC: O(1)