class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        q = deque()

        def add(r,c):

            if board[r][c] == "O":
                board[r][c] = "#"
                q.append((r,c))

        for r in range(rows):
            add(r,0)
            add(r, cols - 1)

        for c in range(cols):
            add(0,c)
            add(rows - 1, c)

        moves = [(0,1), (1,0), (0,-1), (-1,0)]

        while q:

            r,c = q.popleft()

            for a, b in moves:
                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"

        


        


