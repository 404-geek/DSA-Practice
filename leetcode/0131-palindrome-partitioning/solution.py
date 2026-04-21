class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        res = []

        def check_palindrome(path):

            return path == path[::-1]
            

        def backtrack(rem_str, path):

            if rem_str == "":
                res.append(path[:])
                return
                
            p = len(rem_str)

            for i in range(p):
                part = rem_str[:i+1]
                if check_palindrome(part):
                    path.append(part)
                    backtrack(rem_str[i+1:], path)
                    path.pop()

        backtrack(s, [])

        return res





        
