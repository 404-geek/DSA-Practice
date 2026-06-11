class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:

        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            
            node = node.children[ch]

        node.end = True
        

    def search(self, word: str) -> bool:

        def dfs(node, i):

            if i == len(word):
                return node.end

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                
                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], i+1)

        return True if dfs(self, 0) else False

        
