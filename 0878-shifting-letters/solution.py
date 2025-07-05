class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        su = sum(shifts)
        res = ""
        run = 0

        for i, st in enumerate(s):

            val = ord(st)+ su - run
            print(val)

            val = ord('a') + (val - ord('a')) % 26


            print(val)

            res+= chr(val)

            run+= shifts[i]

        
        return res

         
            
        
