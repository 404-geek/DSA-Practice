class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:

        n = len(grid)
        island_id = 2
        areas = {}
        
        for r in range(n):
            for c in range(n):

                if grid[r][c] == 1:
                    q = deque([(r,c)])
                    grid[r][c] = island_id

                    area = 0

                    while q:
                        area +=1

                        row, col = q.popleft()

                        for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)]:

                            nr = row + dr
                            nc = col + dc

                            if  (0 <= nr < n and
                                0 <= nc < n and 
                                grid[nr][nc] == 1
                            ):
                            
                                grid[nr][nc] = island_id
                                q.append((nr,nc))

                    areas[island_id] = area
                    island_id += 1

        max_size = 0

        has_zero = False

        for r in range(n):
            for c in range(n):

                if grid[r][c] == 0:
                    has_zero = True

                    seen = set()
                    current_size = 1

                    for dr,dc in [(-1,0), (1,0), (0,1), (0, -1)]:

                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < n and  0 <= nc < n:

                            island_id = grid[nr][nc]
                            
                            if island_id > 1 and island_id not in seen:

                                seen.add(island_id)
                                current_size += areas[island_id]
                                
                    max_size = max(max_size, current_size)

        if not has_zero:
            return n * n
        
        return max_size



     
 

                    
