class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        curr_sum = 0
        store = {0: -1}

        for i, val in enumerate(nums):

            curr_sum+=val

            rem = curr_sum % k if k != 0 else curr_sum

            if rem in store:
                if i - store[rem] >= 2:
                    return True
            
            else:
                store[rem] = i 
        
        return False



            


        
