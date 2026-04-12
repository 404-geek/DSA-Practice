class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map = {0:1}
        curr = 0
        ans = 0

        for r in nums:

            curr+=r

            ans+= map.get(curr - k, 0)
            
            map[curr] = map.get(curr, 0) + 1
        
        return ans
                






            

        
