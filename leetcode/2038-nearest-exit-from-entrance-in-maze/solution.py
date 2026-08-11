class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        er,ec = entrance[0], entrance[1]
        rows = len(maze)
        cols = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[er][ec] = "#"

        moves = [(0,1), (0,-1), (-1,0), (1,0)]

        while queue:

            r, c, steps = queue.popleft()

            if steps > 0 and (
                r == 0 or r == rows - 1 or
                c == 0 or c == cols - 1
            ):
                return steps
            
            for a,b in moves:
                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0<= nc < cols and maze[nr][nc] == ".":
                    maze[nr][nc] = "#"
                    queue.append((nr, nc, steps + 1))
            
        return -1

        
        
