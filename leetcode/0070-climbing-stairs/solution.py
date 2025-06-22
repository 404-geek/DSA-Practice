class Solution:
    def climbStairs(self, n: int) -> int:

        o, t = 1,1

        for _ in range(n-1):

            temp = t
            t = o+ t
            o = temp

        return t

        
        
