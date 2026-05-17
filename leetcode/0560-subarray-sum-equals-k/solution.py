class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cnt = 0
        curr = 0

        map = {0:1}

        for n in nums:

            curr+=n
            
            if curr - k in map:
                cnt += map[curr - k]

            if curr in map:
                map[curr]+=1
            else:
                map[curr] = 1

        return cnt

        


        
