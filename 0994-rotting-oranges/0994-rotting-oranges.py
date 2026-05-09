class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        q = deque()
        fresh = 0
        time = 0

        # Count fresh oranges and add rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rowd = r + dr
                    cold = c + dc
                    # Check boundaries and fresh orange
                    if (
                        rowd < 0 or rowd >= rows or
                        cold < 0 or cold >= cols or
                        grid[rowd][cold] != 1
                    ):
                        continue

                    # Make orange rotten
                    grid[rowd][cold] = 2

                    # Add new rotten orange
                    q.append((rowd, cold))

                    # Reduce fresh count
                    fresh -= 1
            # One minute completed
            time += 1    

        # If fresh oranges still remain
        return time if fresh == 0 else -1

#TC: O(m*n)
#SC: O(m*n)

        