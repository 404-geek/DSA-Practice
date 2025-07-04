class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        forbidden = set(forbidden)

        MAX_POS = 6000

        i = 0
        pos = 0

        q = deque()
        q.append((0,False))
        v = set((0,False))

        while q:

            for _ in range(len(q)):

                pos, uback = q.popleft()

                if pos == x:
                    return i 

                
                new = pos + a

                if new not in forbidden and (new, False) not in v and 0 <= new <= MAX_POS:

                    q.append((new, False))
                    v.add((new, False))

                back  = pos -b

                if not uback and back >= 0  and (back, True) not in v and back not in  forbidden:
                    q.append((back, True))
                    v.add((back, True))

            i+=1

        return -1

        






