class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t = Counter(t)
        n = len(t)
        trav = defaultdict(int)
        have = 0

        start = 0
        min_len = float(inf)
        min_str = ""

        for end in range(len(s)):
            c = s[end]
            trav[c]+=1

            if c in t and trav[c] == t[c]:
                have+=1

            while have == n:

                if end - start + 1 < min_len:
                    min_str = s[start:end+1]
                    min_len = end - start + 1
                    
                trav[s[start]]-=1
                if s[start] in t and trav[s[start]] < t[s[start]]: 
                    have-=1
                start+=1                    

        return min_str

