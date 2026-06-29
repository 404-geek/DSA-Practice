class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        q = deque([])

        def add(r,c):
            if grid[r][c] == 1:
                grid[r][c] = "#"
                q.append((r,c))

        for r in range(rows):
            add(r,0)
            add(r, cols - 1)

        for c in range(cols):
            add(0, c)
            add(rows - 1, c)

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:

            r,c = q.popleft()

            for a,b in moves:

                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = "#"
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt+=1

        return cnt


            


            








        
