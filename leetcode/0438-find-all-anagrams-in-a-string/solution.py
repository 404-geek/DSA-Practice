class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        start = 0
        an_count = Counter(p)
        n = len(an_count)
        s_len = len(p)
        have = 0
        res = []

        state = defaultdict(int)


        for end in range(len(s)):

            state[s[end]]+=1

            if s[end] in an_count and state[s[end]] == an_count[s[end]]:
                have+=1

            if end - start + 1 == s_len:

                if have == n:

                    res.append(start)

                if s[start] in an_count and state[s[start]] == an_count[s[start]]:
                    have-=1
                state[s[start]] -=1               
                start+=1

        return res




        
