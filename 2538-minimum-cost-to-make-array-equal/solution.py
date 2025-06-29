class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        total_cost = sum(cost)
        res = 0
        acc = 0

        for i in sorted(zip(nums, cost)):
            acc += i[1]
            if acc >= (total_cost //2)+1 :
                target = i[0]
                break

        for i in zip(nums,cost):

            res += (abs(i[0]-target) * i[1])

        return res


        
