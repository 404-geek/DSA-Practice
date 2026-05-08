class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        k = n * 2
        res = []
        
        def gen_formed(path, o_cnt, c_ont):

            if len(path) == k:
                res.append("".join(path))

            if o_cnt < n:
                path.append("(")
                gen_formed(path, o_cnt+1, c_ont)
                path.pop()

            if c_ont < o_cnt:
                path.append(")")
                gen_formed(path, o_cnt, c_ont+1)
                path.pop()

        gen_formed([], 0, 0)

        return res
