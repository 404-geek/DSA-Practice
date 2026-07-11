class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        
        stack = []

        for par in s:

            if par in map:

                stack.append(par)
            
            else:
                if not stack:
                    return False

                if map[stack[-1]] != par:
                    return False

                stack.pop()

        return not stack
                
