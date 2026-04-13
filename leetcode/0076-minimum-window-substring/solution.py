from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n_map = Counter(t)
        need = len(n_map)
        n = len(s)
        have = 0

        ans = ""

        res = defaultdict(int)

        i = 0

        for j in range(n):

            res[s[j]] += 1

            if s[j] in n_map and res[s[j]] == n_map[s[j]]:
                have+=1
                
            while have == need:

                if ans == "" or j - i + 1 < len(ans):
                    ans = s[i : j + 1]
                
                res[s[i]]-=1
                if s[i] in n_map and res[s[i]] < n_map[s[i]]:
                    have-=1
                i+=1

        return ans




        
        
