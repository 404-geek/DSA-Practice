class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxes = defaultdict(set)

        for i in range(9):

            temp_set = set()
            for j in range(9):
       
                val = board[i][j]

                if val == '.':
                    continue


                if val in temp_set:
                    return False
                    
                temp_set.add(board[i][j])

        
        for j in range(9):

            temp_set = set()
            for i in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                if val in temp_set:
                    return False
                temp_set.add(board[i][j])
                    
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                box_id = (i//3, j//3)

                if val in boxes[box_id]:
                    return False
                boxes[box_id].add(val)

        return True
