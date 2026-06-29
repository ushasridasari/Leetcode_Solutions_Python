class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        #Sets the left boundary to 0 and the right boundary to the number of columns.
        l, r = 0, len(matrix[0])
        #Sets the top boundary to 0 and the bottom boundary to the number of rows.
        top, bottom = 0, len(matrix)

        #Keep moving in a spiral as long as there are rows and columns left.
        while l < r and top < bottom:
            #Moving from left to right
            #Loop through the columns from left to right.
            for i in range(l, r):
                #adding each no. from top row to the res
                res.append(matrix[top][i])
            #Move the top boundary down because that row is finished
            top += 1
            #Move from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1
            #Check if Any Rows or Columns Are Left
            if not (l < r and top < bottom):
                break
            #Move from left to right
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            ##Move from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res

    #TC: O(m*n)
    #SC: O(m*n)

