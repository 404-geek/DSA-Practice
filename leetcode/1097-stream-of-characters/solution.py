class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class StreamChecker:

    def __init__(self, words: List[str]):

        self.max_len = 0
        self.root = self.create_Trie(words)
        self.stream = ""

    def create_Trie(self, words):

        root = TrieNode()
        for word in words:
            self.max_len = max(self.max_len, len(word))
            word = reversed(word)
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
            node.end = True

        return root

    def query(self, letter: str) -> bool:

        self.stream += letter

        if len(self.stream) >= self.max_len:
            self.stream = self.stream[-self.max_len:]

        n = len(self.stream)

        node = self.root

        for i in range(n-1, -1, -1):

            ch = self.stream[i]

            if ch not in node.children:
                return False
            
            node = node.children[ch]

            if node.end:
                return True
        
        return False

        
                
        






        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
