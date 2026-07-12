class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for n in arr:

            if n > k:
                break
            
            k+=1

        return k

