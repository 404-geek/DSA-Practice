class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        si = 0

        for i in t:
            try:
                if s[si] == i:
                    si+=1
            except:
                break

        print(si)

        if si == len(s):
            return True
        return False 
