class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        bananas = set()
        res = 0

        q = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bananas.add((r,c))

                elif grid[r][c] == 2:
                    q.append((r,c,0))
        
        if not bananas:
            return 0

        moves = [(-1,0), (1,0), (0,1), (0,-1)]

        def bfs(q, bananas):

            min_time = -1

            while q:

                for i in range(len(q)):

                    r,c, tm  = q.popleft()
                    min_time = tm

                    for a,b in moves:

                        nr = a + r
                        nc = b + c

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2

                            bananas.remove((nr,nc))
                            q.append((nr,nc, tm+1))


            if bananas:
                return -1
            else:
                return min_time

        res = bfs(q, bananas)

        return res
                        
                


            

