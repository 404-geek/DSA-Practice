class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def find_pow(n):

            if n == 0:
                return 1

            half = find_pow(n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return x * half * half


        if n < 0:
            return 1 / find_pow(-n)
        
        return find_pow(n)





