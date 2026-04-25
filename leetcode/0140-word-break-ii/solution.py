class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        mem = {}

        def dfs(i):

            if i == len(s):
                return [""]
            
            if i in mem:
                return mem[i]

            res = []

            for word in word_set:
                l = len(word)
                if s[i: i + l] == word:

                    rem_pos = dfs(i+ l)

                    for w in rem_pos:
                        if w == "":
                            res.append(word)

                        else:
                            res.append(word + " " + w)

            mem[i] = res
            return res

        return dfs(0)

        

        






