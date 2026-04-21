from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def solve(i: int) -> bool:
            if i == len(empties):
                return True

            r, c = empties[i]
            box = (r // 3) * 3 + (c // 3)

            for n in range(1, 10):
                num = str(n)

                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    continue

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if solve(i + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        solve(0)
