class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        arr = []
        zero_count = 0
        for i in nums:
            if i != 0:
                prod*=i
            else:
                zero_count+=1
        
        for i in nums:
            if zero_count > 1:
                arr.append(0)
            elif zero_count == 1:
                if i== 0:
                    arr.append(prod)
                else:
                    arr.append(0)
            else:
                arr.append(prod // i)
        

        return arr
        
