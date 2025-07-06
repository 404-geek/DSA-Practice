class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(i,j):

            pal_s = s[i:j]

            if pal_s == pal_s[::-1]:
                return True
            else:
                return False

        if len(s) == 1:
            return [[s]]

        res = []
        parts = []


        def backtrack(i):

            if i == len(s):
                res.append(parts[:])
                return

            for j in range(i, len(s)):

                if is_palindrome(i,j+1):
                    parts.append(s[i:j+1])
                    backtrack(j+1)
                    parts.pop()
                
        
        backtrack(0)
        return res
                








                        
        
