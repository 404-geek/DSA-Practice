class Solution:
    def largestVariance(self, s: str) -> int:

        f1 = 0
        f2 = 0

        max_var = 0

        pairs = [(i, j) for i in set(s) for j in set(s) if i!=j]

        for _ in range(2):
            for pair in pairs:
                f1, f2 = 0,0

                for letter in s:
                    if letter not in pair:continue

                    if letter == pair[0]: f1+=1

                    if letter == pair[1]: f2+=1

                    if f2 > f1: f1 = f2 = 0

                    elif f1 > 0 and f2 > 0:
                        max_var = max(f1-f2, max_var)

            s = s[::-1]

        return max_var


            
        
