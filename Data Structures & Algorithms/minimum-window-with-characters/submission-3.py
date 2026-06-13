class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t = Counter(t)

        have = 0

        res = ""
        le = len(s) + 1

        i = 0

        run_map = defaultdict(int)

        for j in range(len(s)):

            run_map[s[j]] += 1

            if run_map[s[j]] == t[s[j]]:
                have+=1

            while have == len(t):

                if j - i + 1 < le:
                    le = j - i + 1
                    res = s[i:j+1]

                run_map[s[i]]-=1

                if s[i] in t and run_map[s[i]] < t[s[i]]:
                    have-=1
                
                i+=1

        return res
                

            




            
        