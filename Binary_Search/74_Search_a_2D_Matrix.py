class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1
        while top <= bot:
            row = (top + bot) // 2
            #if target is greater than the last element of the middle row
            if target > matrix[row][-1]:
                #moves top down to row + 1 because the target must be in a lower row.
                top = row + 1
            elif target < matrix[row][0]:
                #moves bot up to row - 1
                bot = row - 1
            else:
                break
                #If top has crossed bot, i.e, target is not in any row
        if not (top <= bot):
            return False
        # final row where the target will be.
        #binary search in a row
        row = (top + bot) // 2
        l, r = 0, col - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
            