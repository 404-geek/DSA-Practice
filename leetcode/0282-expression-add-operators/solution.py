class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        res = []
        n = len(num)
        
        def traverse(i, path, t, prev):

            if i == n and t == target:
                res.append("".join(path))
                return

            for j in range(i, n):

                curr_str = num[i:j+1]

                if len(curr_str) > 1 and curr_str[0] == "0":
                    break

                curr = int(num[i:j+1])

                path.append("+")
                path.append(curr_str)
                traverse(j+1, path, t + curr, curr)
                path.pop()
                path.pop()

                path.append("-")
                path.append(curr_str)
                traverse(j+1, path, t - curr, -curr)
                path.pop()
                path.pop()

                path.append("*")
                path.append(curr_str)
                traverse(j+1, path, prev * curr + t - prev, prev * curr)
                path.pop()
                path.pop()

        for j in range(0, n):
            curr_str = num[0:j+1]

            if len(curr_str) > 1 and curr_str[0] == "0":
                break

            curr = int(curr_str)
            traverse(j + 1, [curr_str], curr, curr)

        return res




        
