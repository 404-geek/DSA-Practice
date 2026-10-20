class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:

            if char == "]":

                a = ""

                while stack:

                    ch = stack.pop()

                    if ch == "[":
                        break
                    
                    a = ch + a

                times = ""

                while stack and stack[-1].isdigit():
                    times = stack.pop() + times

                a = a * int(times)

                stack.append(a)
            
            else:
                stack.append(char)
            
        return "".join(stack)



                


                







