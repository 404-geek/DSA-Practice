class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []

        wordDict = set(wordDict)

        def traverse(path, i):

            if i == len(s):
                res.append(" ".join(path))
                return

            for j in range(i, len(s)+1):

                if s[i:j] in wordDict:
                    path.append(s[i:j])
                    traverse(path, j)
                    path.pop()
        
        traverse([],0)

        return res

            
        