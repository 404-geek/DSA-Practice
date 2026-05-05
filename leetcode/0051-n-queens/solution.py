class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        res = []

        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def traverse_row(r):
            if r == n:
                res.append(["".join(row) for row in grid])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                grid[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                traverse_row(r + 1)

                grid[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        traverse_row(0)
        return res
