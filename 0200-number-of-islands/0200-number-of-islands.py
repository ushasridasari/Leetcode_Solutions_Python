class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Stores 4 possible movement directions
        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        #Number of rows and columns
        rows, cols = len(grid), len(grid[0])
        #Stores total Island count
        islands = 0

        def dfs(r, c):
            if ( r < 0 or r >=rows or c >=cols or c < 0 or grid[r][c] == "0"):
                return
            #Convert land into water after visiting, so we no need to visit again
            grid[r][c] = "0"
            #Loop through all directions.
            for dr, dc in directions:
                #Visit neighboring cells.
                dfs(r+dr, c+dc)
        #Loop through all rows and columns
        for r in range(rows):
            for c in range(cols):
                #if we found unvisited land.
                if grid[r][c] == "1":
                    #Explore entire connected island.
                    dfs(r, c)
                    #Increase island count
                    islands += 1

        return islands
#TC: O(m*n)
#SC: O(m*n)
        
        