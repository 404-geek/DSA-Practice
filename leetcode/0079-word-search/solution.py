class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        n = len(word)

        def traverse(r,c, i):

            if i == n - 1:
                return True

            a = board[r][c]

            board[r][c] = '#'

            moves = [(0,-1), (0,1), (1,0), (-1,0)]

            for p, q in moves:

                nr = r + p
                nc = c + q

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[i+1]:
                    if traverse(nr, nc, i+1):
                        board[r][c] = a
                        return True

            board[r][c] = a

            return False

        i = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[i]:
                    if traverse(r, c, i):
                        return True
        
        return False
            
        
