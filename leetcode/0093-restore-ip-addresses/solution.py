class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def is_valid(num):
            if not num:
                return False
            if len(num) > 1 and num[0] == '0':
                return False

            return int(num) <= 255

        def backtrack(s, groups, path):

            if groups == 4:
                if s == "":
                    res.append(".".join(path))
                return 

            for i in range(1,4):
                if i <= len(s):
                    part = s[:i]

                    if is_valid(part):
                        path.append(part)
                        backtrack(s[i:], groups + 1, path)
                        path.pop()

        backtrack(s, 0, [])
        return res

