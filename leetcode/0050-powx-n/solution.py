class Solution:
    def myPow(self, x: float, n: int) -> float:

        # def pow(x,n):

        #     if n == 0:
        #         return 1

        #     half = pow (x, n // 2)

        #     if n % 2 == 0:
        #         return half * half
            
        #     else:
        #         return x * half * half

        
        if n < 0:
            x = 1/ x
            n = -n

        ans = 1

        while n > 0:

            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        return ans


        
