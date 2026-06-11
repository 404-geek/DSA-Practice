class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        root = TrieNode()

        res = []

        words.sort(key=len)

        def insert(word):

            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.end = True

        for word in words:

            @cache
            def dfs(i):

                if i == len(word):
                    return True

                node = root

                for j in range(i, len(word)):

                    ch = word[j]

                    if ch not in node.children:
                        return False

                    node = node.children[ch]

                    if node.end and dfs(j+1):
                        return True

                return False

            if dfs(0):
                res.append(word)

            insert(word)

        return res

        return res


        
    
