class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        n = len(num)
        res = []

        def traverse(i, path, su, prev):
            if i == n:
                if su == target:
                    res.append(path)
                return

            for j in range(i, n):
                
                st = num[i:j+1]

                if j-i+1 > 1 and st[0] == "0":
                    break

                val = int(st)

                traverse(j+1, path + "+" + st, su + val, val)
                traverse(j+1,  path + "-" + st, su - val, -val)
                traverse(j+1, path + "*" + st, (val * prev) + (su - prev),  prev * val)
        

        for i in range(1,n+1):
            st = num[:i]
            
            if i > 1 and st[0] == "0":
                break

            val = int(st)
            traverse(i, st, val, val)

        return res



                

