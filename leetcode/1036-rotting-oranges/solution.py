class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        min = 0

        q = Deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        move = [(0,1), (0,-1), (1,0), (-1,0)]

        while q and fresh > 0:

            for _ in range(len(q)):

                r, c = q.popleft()

                for a, b in move:
                    nr = a + r
                    nc = b + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh-=1

            min+=1

        return min if fresh == 0 else -1





