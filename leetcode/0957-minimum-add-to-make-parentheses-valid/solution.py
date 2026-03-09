class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        balance = 0
        min_moves = 0

        for i in s:

            if i == "(":
                balance +=1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    min_moves+=1
        
        return min_moves + balance                    

        


        
