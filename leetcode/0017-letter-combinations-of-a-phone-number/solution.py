class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map = {'2' : "abc", '3': "def",
              '4' : "ghi", '5' : "jkl", '6': "mno",
              '7' : "pqrs", '8' : "tuv", '9': "wxyz" }
        
        k = len(digits)

        res = []
        
        def backtrack(ind, path):
            if ind == k:
                res.append(path)
                return

            letters = map[digits[ind]]

            for ch in letters:
                backtrack(ind + 1, path+ch)
            
        
        backtrack(0, "")
        return res

            





