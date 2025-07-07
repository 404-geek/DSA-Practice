class Solution:


    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(m,n, s):

            if s == len(word):
                return True
            
            if m < 0 or m >= r or n < 0 or n >= c:
                return False

            if board[m][n] != word[s]:
                return False

            temp = board[m][n]
            board[m][n] = "#" 

            found = (dfs(m+1, n, s+1) or
                    dfs(m-1, n, s+1) or
                    dfs(m, n+1, s+1) or
                    dfs(m, n-1, s+1))

            board[m][n] = temp
            return found
 
        
        r,c = len(board), len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False
