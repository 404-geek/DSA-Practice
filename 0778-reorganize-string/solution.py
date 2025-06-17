class Solution:
    def reorganizeString(self, s: str) -> str:

        n = len(s)
        freq = Counter(s)
        max_char, max_freq = max(freq.items(), key=lambda x: x[1])
        
        # Check if solution is possible
        if max_freq > (n + 1) // 2:
            return ""
        
        res = [""] * n
        i = 0
        
        # Place most frequent character first
        for _ in range(freq[max_char]):
            res[i] = max_char
            i += 2
        freq[max_char] = 0
        
        # Place the rest of the characters
        for char, count in freq.items():
            for _ in range(count):
                if i >= n:
                    i = 1  # switch to odd indices
                res[i] = char
                i += 2

        return ''.join(res)
        
