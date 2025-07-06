class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        ds = defaultdict(int)
        dp = defaultdict(int)

        if len(s) != len(t):
            return False

        for i,j in zip(s,t):

            if i in ds:
                if ds[i] != j:
                    return False
            else:
                ds[i] = j

            if j in dp:
                if dp[j] != i:
                    return False
            else:
                dp[j] = i


        return True
        
