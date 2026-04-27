class Trie:

    def __init__(self):

        self.map = defaultdict(Trie)
        self.end = False
        
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.map[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch in node.map:
                node = node.map[ch]
            else:
                return False

        return True if node.end == True else False

    def startsWith(self, prefix: str) -> bool:

        node = self
        for ch in prefix:
            if ch in node.map:
                node = node.map[ch]
            else:
                return False

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
