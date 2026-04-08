class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        

        res = []
        def backtrack(i , path):

            if i == len(digits):
                print(path)
                res.append(path)
                return

            for ch in digit_to_letters[digits[i]]:
                backtrack(i+1, path + ch)

        backtrack(0, "")
        
        return res
