class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ma = defaultdict(int)
        mx = 0
        i = 0

        for j in range(len(s)):

            ma[s[j]]+=1

            while ma[s[j]] > 1:
            
                ma[s[i]] -=1
                if ma[s[i]] == 0:
                    del ma[s[i]]
                i+=1

            mx = max(mx, j - i + 1)

        return mx
        
