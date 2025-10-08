class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        start = 0
        max_len = 0
        state = defaultdict(int)
        max_freq = 0

        for end in range(len(s)):

            state[s[end]] +=1

            max_freq = max(state[s[end]], max_freq)

            if k + max_freq < end - start + 1:
                state[s[start]]-=1
                start+=1

            max_len = max(max_len, end - start+1)


        return max_len

        
