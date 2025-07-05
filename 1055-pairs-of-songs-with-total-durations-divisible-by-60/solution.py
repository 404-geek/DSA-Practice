class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        rem = defaultdict(int)
        cnt = 0
        for t in time:
            
            r = t % 60


            comp = (60 -  r) %60 
            cnt+= rem[comp]

            rem[r]+=1
 
        
        return cnt
