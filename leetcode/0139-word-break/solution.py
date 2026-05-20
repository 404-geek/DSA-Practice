class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        max_len = 0

        for w in wordDict:
            max_len = max(len(w), max_len)
        
        wordDict = set(wordDict)
        n = len(s)

        @cache
        def traverse(i):
            if i == n:
                return True

            for j in range(i, min(n, i + max_len)):

                part = s[i:j+1]
                if part in wordDict:
                    if traverse(j+1):
                        return True

            return False

        return traverse(0)
