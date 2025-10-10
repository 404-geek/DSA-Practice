class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_count = Counter(p)
        p_len = len(p)

        start = 0
        res = []
        state = defaultdict(int)

        have = 0

        for end in range(len(s)):

            state[s[end]]+=1

            if s[end] in p_count and state[s[end]] == p_count[s[end]]:

                have+=1

            if end - start + 1 == p_len:

                if have == len(p_count):
                    res.append(start)
                
                if s[start] in p_count and state[s[start]] == p_count[s[start]]:
                    have-=1
                state[s[start]]-=1
                start+=1
            
        return res

                








        
