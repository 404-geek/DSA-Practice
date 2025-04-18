class Solution:
    def numberOfWays(self, s: str) -> int:

        total_0 = s.count("0")
        total_1 = s.count("1")

        left_0 = 0
        left_1 = 0
        result = 0

        for i in s:

            if i == "0":
                ways = (left_1)  * (total_1 - left_1)
                left_0+=1
                result+=ways
            
            else:
                ways = (left_0)  * (total_0 - left_0)
                left_1+=1
                result+=ways

        return result
                
            





        
