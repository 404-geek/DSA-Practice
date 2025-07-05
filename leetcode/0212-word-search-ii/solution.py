class TrieNode:

    def __init__ (self):

        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:

    def addwords(self, words):

        root = TrieNode()

        for word in words:
            node= root

            for ch in word:
                node = node.children[ch]
            node.word =  word
        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = self.addwords(words)
        result = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            child = node.children[ch]

            if child.word:
                result.append(child.word)
                child.word = None  # Avoid duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, child)
            board[r][c] = ch  # restore after backtrack

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result



            
        
        
