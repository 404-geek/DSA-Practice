class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_l = ''

        def check_palindrome(left, right):

            while left >=0  and right < len(s) and s[left] == s[right]:

                left-=1
                right+=1

            return left+1, right-1

        l, r = 0,0
        
        for i in range(len(s)):

            a, b = check_palindrome(i, i)

            c, d = check_palindrome(i, i+1)


            if b-a > r - l:
                l ,r = a,b
            if d-c > r-l:
                l, r = c, d

        
        return s[l:r+1]


        
