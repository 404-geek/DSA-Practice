class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        sy = Counter(s)

        for i,m in enumerate(s):

            if sy[m] == 1:
                return i
        
        return -1


