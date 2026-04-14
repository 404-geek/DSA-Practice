class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        start = word[0]

        l_word = len(word)

        move = [[0,-1], [0,1], [1,0], [-1,0]]
        

        def traverse(r,c, l, vis):

            if l == l_word - 1:
                return True

            vis.add((r,c))

            for i , j in move:

                nr = i + r
                nc = j + c

                if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in vis and board[nr][nc] == word[l+1]:
                    if traverse(nr,nc, l+1, vis):
                        return True

            vis.remove((r,c))

            return False


        for r in range(row):
            for c in range(col):
                if board[r][c] == start:
                    if traverse(r,c,0, set()):
                        return True

        return False
