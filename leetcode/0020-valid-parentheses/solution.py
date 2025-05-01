class Solution:
    def isValid(self, s: str) -> bool:

        left_brac = ['(', '{', '[']
        right_brac = [')', '}', ']']

        map = {}
        i = 0
        while i < len(left_brac):

            map[right_brac[i]] = left_brac[i]
            i+=1

        set_l = set(left_brac)

        stack = []

        for i in s:

            if i in set_l:
                stack.append(i)
            else:
                if not stack or stack.pop() != map[i]:
                    return False
                
        return not stack


        
