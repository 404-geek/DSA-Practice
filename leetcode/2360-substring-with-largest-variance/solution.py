class Solution:
    def largestVariance(self, s: str) -> int:

        res = 0
        freq = {c: s.count(c) for c in set(s)}

        for a in freq:
            for b in freq:
                if a == b:
                    continue

                var = 0
                has_b = False
                remain_b = freq[b]

                for ch in s:
                    if ch != a and ch != b:
                        continue
                    
                    if ch == a:
                        var += 1
                    elif ch == b:
                        var -= 1
                        remain_b -= 1
                        has_b = True

                    if has_b:
                        res = max(res, var)
                    
                    if var < 0 and remain_b > 0:
                        var = 0
                        has_b = False

        return res


            
        
