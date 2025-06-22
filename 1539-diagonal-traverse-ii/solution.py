class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        i, j = 0,0
        map = defaultdict(list)
        res = []
        while i < len(nums):
            j = 0
            while j < len(nums[i]):
                map[i+j].append(nums[i][j])

                j+=1
            
            i+=1

        print(map)

        for i in map:

            res+=map[i][::-1]

        return res





        
