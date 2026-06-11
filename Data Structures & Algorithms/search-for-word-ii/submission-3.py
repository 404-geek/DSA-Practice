
class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        node = TrieNode()

        rows = len(board)
        cols = len(board[0])

        res = []

        moves = [(-1,0), (0,-1), (1,0), (0,1)]

        for word in words:

            root = node

            for ch in word:

                if ch not in root.children:
                    root.children[ch] = TrieNode()

                root = root.children[ch]
            
            root.end = True

        def dfs(r,c, node, path):

            if node.end:
                res.append("".join(path))
                node.end = False
            
            for move in moves:

                a, b = move
                nr = a + r
                nc = b + c

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node.children:
                    ch = board[nr][nc]
                    board[nr][nc] = "#"
                    path.append(ch)
                    dfs(nr,nc, node.children[ch], path)
                    path.pop()
                    board[nr][nc] = ch

            return


        for r in range(rows):
            for c in range(cols):
                if board[r][c] in node.children:
                    ch = board[r][c]
                    board[r][c] = "#"
                    dfs(r,c, node.children[ch],[ch])
                    board[r][c] = ch

        return res

        

        





