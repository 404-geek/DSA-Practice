class Solution:
    def myAtoi(self, s: str) -> int:

        def recurse(i, num):

            if i == n or not s[i].isdigit():
                return num

            return recurse(i+1, num * 10 + int(s[i]))
        
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0

        # num = recurse(i, num)

        while i < n and s[i].isdigit():

            num = num * 10 + int(s[i])
            i+=1

        num *= sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
        
              
        
