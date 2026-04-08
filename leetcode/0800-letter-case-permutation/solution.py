class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []


        def backtrack(i, path):

            if i == len(s):
                res.append(path)
                return

            if s[i].isdigit():
                backtrack(i+1, path + s[i])
            
            else:
                backtrack(i+1, path + s[i].lower())
                backtrack(i+1, path + s[i].upper())

        backtrack(0, "")

        return res
        
