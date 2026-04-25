class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        q = Deque([(beginWord, 1)])

        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        while q:

            for _ in range(len(q)):

                word, l = q.popleft()

                if word == endWord:
                    return l

                for i in range(len(word)):

                    for j in 'abcdefghijklmnopqrstuvwxyz':

                        new_w = word[:i] + j + word[i+1:]

                        if new_w in wordList:
                            wordList.remove(new_w)
                            q.append((new_w, l+1))

        return 0

                        





                 

            

        

        
