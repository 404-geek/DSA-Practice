class TrieNode():
    def __init__(self):
        self.children = {}

class Solution:
    def countDistinctSubstring(self, s):
        # Your code goes here

        root = TrieNode()
        count = 1

        for i in range(len(s)):

            node = root
            
            for j in range(i, len(s)):

                v = s[j]

                if v not in node.children:
                    node.children[v] = TrieNode()
                    count+=1
                node = node.children[v]

        return count