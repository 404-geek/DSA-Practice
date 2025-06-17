class Solution:
    def countBinarySubstrings(self, s: str) -> int:


        prev = 0
        res = 0
        curr = 1

        for i in range(1,len(s)):

            if s[i] != s[i-1]:
                res += min(prev, curr)

                prev = curr
                curr = 1
            else:
                curr+=1

        return res + min(prev, curr)
