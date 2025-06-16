class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        sr = ['b', 'a', 'l', 'o', 'n']
        sr_dict = {}

        for i in text:
            if i in sr:
                sr_dict[i] = sr_dict.get(i, 0) + 1

        if len(sr_dict) < 5:
            return 0
        


        required = Counter("balloon")
        return min(sr_dict.get(c, 0) // required[c] for c in required)
            

        





