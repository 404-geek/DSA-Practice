class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = ""
        mi = 0

        for i in range(n):

            m = s[i]

            j = i
            k = i


            while j >= 0 and k <n and s[j] == s[k]:

                if k - j + 1 >= mi:
                    mi = k - j + 1
                    ans = s[j:k+1]

                k+=1
                j-=1

            
            j = i
            k = i+1

            while j >= 0 and k < n and s[j] == s[k]:

                if k - j + 1 > mi:
                    mi = k - j + 1
                    ans = s[j:k+1]
                
                j-=1
                k+=1

        return ans
    

            
                
