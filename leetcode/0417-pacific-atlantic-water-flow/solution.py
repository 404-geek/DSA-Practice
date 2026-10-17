class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        m = len(heights[0])
        n = len(heights)

        q = deque([(0,m-1), (n-1,0)])

        

        moves = [(0,-1), (-1,0), (1,0), (0,1)]

        def traverse(q,vis):

            while q:

                r,c = q.popleft()

                for a,b in moves:

                    nr = r + a
                    nc = b + c

                    if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in vis and heights[nr][nc] >= heights[r][c]:

                        vis.add((nr,nc))
                        q.append((nr,nc))


        pacific_q = deque()
        atlantic_q = deque()

        pacific_vis = set()
        atlantic_vis = set()


        for r in range(n):

            pacific_q.append((r,0))
            atlantic_q.append((r,m-1))

            pacific_vis.add((r,0))
            atlantic_vis.add((r,m-1))

        
        for c in range(m):
            pacific_q.append((0,c))
            atlantic_q.append((n-1,c))

            pacific_vis.add((0, c))
            atlantic_vis.add((n-1, c))

        traverse(pacific_q, pacific_vis)
        traverse(atlantic_q, atlantic_vis)

        res = []

        for r, c in atlantic_vis & pacific_vis:
            res.append([r,c])

        return res

            



