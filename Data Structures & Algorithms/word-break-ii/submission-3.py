from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        max_len = max(len(word) for word in wordDict)
        wordDict = set(wordDict)

        @cache
        def dfs(i):

            if i == len(s):
                return [""]

            res = []

            for j in range(i+1, min(len(s), i + max_len) + 1):

                word = s[i:j]

                if word in wordDict:

                    for suffix in dfs(j):
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)    
            
            return res
        
        return dfs(0)

            
        