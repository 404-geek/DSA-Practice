class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        n = len(s)

        @cache
        def traverse(i):

            if i == n:
                return True

            for word in wordDict:
                if s.startswith(word, i):
                    if traverse(i + len(word)):
                        return True

            return False

        return traverse(0) 
            



        
