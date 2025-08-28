class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        

        lsum = sum(cardPoints[:k])

        rsum  = 0 
        si = len(cardPoints)

        max_sum = lsum

        for i in range(k -1 , -1, -1):

            if i == -1:
                lsum = 0
            else:
                lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[si-1]
            si-=1

            max_sum = max (max_sum, lsum+rsum)

        return max_sum


