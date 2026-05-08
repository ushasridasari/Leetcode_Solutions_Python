class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Stores 4 movement directions
        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        #length of rows and cols
        rows, cols = len(grid), len(grid[0])
        #Stores the largest island area found
        area = 0
        #BFS to calculate island area
        def bfs(r, c):
            #Creates a queue for BFS traversal
            q = deque()
            #Marks the cell as visited
            grid[r][c] = 0
            #Adds first land cell into queue
            q.append((r, c))
            #Area starts with 1 cell
            res = 1
            #ontinues BFS while queue has cells
            while q:
                #
                row, col = q.popleft()
                #Loops through all neighboring direction
                for dr, dc in directions:
                    #Calculates neighbor position.
                    nr, nc = dr + row, dc + col
                    #Checks whether neighbor is invalid or water.
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or grid[nr][nc] == 0
                    ):
                        #Skips invalid neighbor
                        continue
                    #Adds neighboring land into queue.
                    q.append((nr, nc))
                    #Marks neighbor as visited.
                    grid[nr][nc] = 0
                    #Increase land area
                    res += 1
            #Returns calculated island area.
            return res
        #Loops through all rows and cols
        for r in range(rows):
            for c in range(cols):
                #If a cell value is 1 ie, land
                if grid[r][c] == 1:
                    #Find island size using BFS and store maximum
                    area = max(area, bfs(r, c))
        #Returns biggest island size.
        return area

#TC : O(m*n)
#SC : O(m*n)
        