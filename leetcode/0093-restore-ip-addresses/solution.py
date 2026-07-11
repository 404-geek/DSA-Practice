class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        n = len(s)
        
        def is_valid(num):
            if len(num) > 1 and num[0] == '0':
                return False

            return int(num) <= 255

        def backtrack(i, groups, path):

            if groups == 4 and i == n:
                res.append(".".join(path))
                return

            remaining_digits = n - i
            remaining_groups = 4 - groups

            if remaining_digits < remaining_groups:
                return

            if remaining_digits > remaining_groups * 3:
                return


            for j in range(i+1, i + 4):

                if j > n:
                    return

                part = s[i:j]

                if is_valid(part):
                    backtrack(j, groups + 1, path + [part])

        backtrack(0, 0, [])
        
        return res

