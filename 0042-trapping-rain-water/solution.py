class Solution:
    def trap(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        left_max = height[i]
        right_max = height[j]
        water = 0

        while i < j:

            if left_max < right_max:

                i+=1
                left_max = max(left_max, height[i])
                water += left_max - height[i]
                

            else:

                j-=1
                right_max = max(right_max, height[j])
                water += right_max - height[j]

        
        return water




        
