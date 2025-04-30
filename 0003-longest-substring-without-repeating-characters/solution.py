class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = set()
        total = 0

        i , j = 0,0 
        while j < len(s):

            if s[j] not in st:
                st.add(s[j])
                total = max(total, j - i + 1)
                j+=1
            else:
                st.remove(s[i])
                i+=1

        return total

        
