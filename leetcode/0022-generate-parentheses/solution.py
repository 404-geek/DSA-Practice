class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def gen(path, i, l , r):

            if i == 2 * n and l == r:
                res.append("".join(path))
                return
            
            if l < n:

                path.append("(")
                gen(path, i + 1, l+1, r)
                path.pop()

            if r < l:

                path.append(")")
                gen(path, i + 1,  l, r+1)
                path.pop()


        gen([], 0, 0,0)

        return res
