class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        i= 0
        j = len(height)-1
        max_l = height[i]
        max_r = height[j]

        total = 0

        while i < j:
            if max_l < max_r:
                i += 1
                max_l = max(max_l, height[i])
                total += max_l - height[i]
            else:
                j -= 1
                max_r = max(max_r, height[j])
                total += max_r - height[j]
            
        return total

            

            


        

