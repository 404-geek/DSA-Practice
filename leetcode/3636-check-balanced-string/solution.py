class Solution:
    def isBalanced(self, num: str) -> bool:

        even_sum = 0
        odd_sum = 0
        start = True

        for n in num:
            
            if start:
                odd_sum+=int(n)
            else:
                even_sum+=int(n)

            start ^= 1

        return even_sum == odd_sum

        
