class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        cols =  len(mat[0])
        rows =  len(mat)

        q = deque([])

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))

                else:
                    mat[r][c] = -1

        moves = [(0,-1),(0, 1), (-1,0), (1,0)]

        while q:

            a,b = q.popleft()

            for r,c in moves:

                nr = a + r
                nc = b + c
                
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[a][b] + 1
                    q.append((nr,nc))

        return mat

                    



        

        
