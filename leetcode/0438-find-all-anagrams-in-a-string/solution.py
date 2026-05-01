class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        c_str = len(p)
        p = Counter(p)

        s_len = len(s)
        run_map = defaultdict(int)

        ans = []
        have = 0

        l = 0

        for r in range(s_len):

            ch = s[r]

            if ch in p:
                run_map[ch]+=1

                if run_map[ch] == p[ch]:
                    have+=1
            
            while r -l + 1 > c_str:
                if s[l] in p:
                    c = s[l]

                    if run_map[c] == p[c]:
                        have-=1
                    run_map[c]-=1
                l+=1
            
            if r-l+1 == c_str and have == len(p):
                ans.append(l)

        return ans        




        
