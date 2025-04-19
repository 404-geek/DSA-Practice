class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        curr = 0
        great = max(candies)
        result = []
        for kid in candies:

            curr = kid + extraCandies
            if curr >= great:
                result.append(True)
            else:
                result.append(False)

        return result



        
