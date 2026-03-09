class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }


        for ch in s:
            if ch in match:
                if not stack or stack.pop() != match[ch]:
                    return False
            else:
                stack.append(ch)


        
        if stack:
            return False
        else:
            return True            


        
