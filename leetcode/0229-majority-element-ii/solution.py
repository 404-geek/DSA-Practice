class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cnt1 = 0
        cnt2 = 0
        ele1 = -109
        ele2 = -190
        si = len(nums)

        for n in nums:
            
            if cnt1 == 0 and n != ele2:
                ele1 = n
                cnt1+=1
            elif cnt2 == 0 and n != ele1:
                ele2 = n 
                cnt2+=1
            elif ele1 == n: cnt1+=1
            elif ele2 == n: cnt2+=1
            else:
                cnt1-=1
                cnt2-=1

        res = []
        cnt1, cnt2 = 0, 0
        for n in nums:

            if n== ele1:
                cnt1+=1
            if n == ele2:
                cnt2+=1

        req =  si // 3

        if cnt1 > req:
            res.append(ele1)
        if cnt2 > req:
            res.append(ele2)

        return res
        
