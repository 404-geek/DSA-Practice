class Solution:
    def myAtoi(self, s: str) -> int:

        n = len(s)
        sign = 1
        i = 0
        res = 0
        MIN_I = - 2 ** 31
        MAX_I = (2 ** 31) - 1

        if not s:
            return 0

        while i < n and s[i] == " ":
                i+=1

        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i+=1

        print(i)
        while i < n and s[i].isdigit():
            res = res* 10 + int(s[i])
            val = sign * res

            if val < MIN_I:
                return MIN_I
            if val > MAX_I:
                return MAX_I

            i += 1

        return sign * res




        

        
