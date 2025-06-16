class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""
        
        chars = list(palindrome)
        n = len(chars)

        for i in range(n//2):

            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)

        chars[-1] = 'b'
        return ''.join(chars)

             

