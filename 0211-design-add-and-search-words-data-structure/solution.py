class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        node = self.root

        for ch in word:

            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:

        stack = [(self.root, 0)]

        while stack:

            node, i = stack.pop()

            if i == len(word):
                if node.is_end:
                    return True
                continue

            ch = word[i]

            if ch == '.':
                for n in node.children.values():
                    stack.append((n, i+1))

            else:
                if ch in node.children:
                    stack.append((node.children[ch], i+1))

        return False


        return dfs(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
