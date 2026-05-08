class Solution:
    def validStrings(self, n: int) -> List[str]:

        res = []

        def valid_choice(path, prev):

            if len(path) == n:
                res.append("".join(path))
                return

            path.append("1")
            valid_choice(path, "1")
            path.pop()

            if prev != "0":
                path.append("0")
                valid_choice(path, "0")
                path.pop()

        
        valid_choice([], "")

        return res


            

                

