class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        visited = set()

        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            exploring_nodes = [(0,1), (-1,0), (1,0),(0,-1)]

            for dr, dc in exploring_nodes:
                nc = c+dc
                nr = r+dr

                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == "1" and (nr, nc) not in visited):
                    dfs(nr, nc)
            
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    result+=1


        return result                    
        
        
        
