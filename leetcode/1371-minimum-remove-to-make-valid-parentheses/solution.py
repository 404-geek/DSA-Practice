class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        remove = set()

        n = len(s)

        for i in range(n):

            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        
        remove.update(stack)

        res = []

        for i in range(n):
            if i not in remove:
                res.append(s[i])

        return "".join(res)


        
