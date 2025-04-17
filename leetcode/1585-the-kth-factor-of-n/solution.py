class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for val in range(1,n+1):
            if n%val == 0:
                k-=1
                if k == 0:
                    return val

        return -1



        
