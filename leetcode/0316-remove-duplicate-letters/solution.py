class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_occur = { c: i for i, c in enumerate(s)}

        stack = []

        seen = set()

        for i, c in enumerate(s):

            if c in seen:
                continue

            while stack and stack[-1] > c and i < last_occur[stack[-1]]:
                a = stack.pop()
                seen.remove(a)

            stack.append(c)
            seen.add(c)

        return "".join(stack)




        
