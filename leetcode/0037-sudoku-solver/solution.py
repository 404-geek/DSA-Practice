class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_idx = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    empty_idx.append((r,c))
                else:
                    val = board[r][c]
                    row_set[r].add(val)
                    col_set[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # def check(ch, r,c):

        #     #Row check
        #     for i in range(9):
        #         if board[r][i] == ch:
        #             return False

        #     #Col check
        #     for i in range(9):
        #         if board[i][c] == ch:
        #             return False

        #     #3x3 matrix check
        #     b_row = (r // 3) * 3
        #     c_row = (c // 3) * 3

        #     for i in range(b_row, b_row+3):
        #         for j in range(c_row, c_row + 3):
        #             if board[i][j] == ch:
        #                 return False

        #     return True


        def traverse(i):

            if i == len(empty_idx):
                return True

            r, c = empty_idx[i]
            box = (r // 3) * 3 + (c // 3)

            for ch in "123456789":

                if ch not in row_set[r] and ch not in col_set[c] and ch not in boxes[box]:
                    board[r][c] = ch
                    row_set[r].add(ch)
                    col_set[c].add(ch)
                    boxes[box].add(ch)

                    if traverse(i+1):
                        return True
                    
                    board[r][c] = "."
                    row_set[r].remove(ch)
                    col_set[c].remove(ch)
                    boxes[box].remove(ch)

            return False

        traverse(0)
                                

        
