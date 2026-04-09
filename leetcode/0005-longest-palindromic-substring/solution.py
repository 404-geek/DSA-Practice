class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mi = 0
        val = ""
        for j in range(n):

            l , r = j, j

            while l >= 0 and r < n and s[l] == s[r]:

                if r - l + 1 >= mi:
                    mi = r - l + 1
                    val = s[l:r+1]
                
                l-=1
                r+=1

            l, r = j, j + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > mi:
                    mi = r - l + 1
                    val = s[l:r+1]
                l -= 1
                r += 1

        return val


            
