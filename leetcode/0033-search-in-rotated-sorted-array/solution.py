class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0
        r = len(nums) - 1

        while l <= r:
            
            pivot = (l+r) //2

            if nums[pivot] == target:
                return pivot

            if nums[l] <= nums[pivot]:

                if nums[l] <= target < nums[pivot]:

                    r = pivot -1
                
                else:
                    l = pivot +1

            else:

                if nums[pivot] < target <= nums[r]:

                    l = pivot + 1
                else:
                    r = pivot -1

        return -1


        
