class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search (arr, target, first):

            low, high = 0, len(arr) - 1

            res = -1

            while low <= high:

                mid = (low + high) // 2

                if arr[mid] == target:
                    res = mid
                    if first:
                        high = mid - 1
                    else:
                        low = mid + 1
                
                elif arr[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            return res
        
        if not nums:

            return [-1,-1]

        f_ind = search(nums, target, first=True)
        l_ind = search(nums, target, first=False)
        
        return [f_ind, l_ind]
