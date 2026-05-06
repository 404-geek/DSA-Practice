class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)

        res = []

        def check_palindrome(s):
            return s == s[::-1]

        def traverse(a, path):

            if a == n:
                res.append(path[:])
                return

            for b in range(a, n):

                part = s[a:b+1]

                if check_palindrome(part):
                    path.append(part)
                    traverse(b+1, path)
                    path.pop()

        traverse(0,[])

        return res





            
        
