class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1

        vis = set()

        q = Deque([('0000', 0)])

        while q:

            for i in range(len(q)):

                code, l = q.popleft()

                if code == target:
                    return l

                for d in range(4):

                    digit = int(code[d])

                    up = (digit + 1) % 10
                    down = (digit - 1) % 10

                    up_str = code[:d] + str(up) + code[d+1:]
                    down_str = code[:d] + str(down) + code[d+1:]

                    for n in [up_str, down_str]:
                        if n not in deadends and n not in vis:
                            vis.add(n)
                            q.append((n, l+1))

        return -1



        
