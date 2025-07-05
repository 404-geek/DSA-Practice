class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        zer_count = 0
        res = 0

        for i in s:

            if i == "1":
                if zer_count > 0:
                    res = max(res+1, zer_count)
            else:
                zer_count+=1


        return res

        
