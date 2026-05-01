class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        map = {}
        
        for i,e in enumerate(edges):
            if e in map:
                map[e] += i
            else:
                map[e] = i
        
        ans = None

        for a, b in map.items():
            if ans is None:
                ans = a
            else:
                if b > map[ans]:
                    ans = a
                elif b == map[ans]:
                    if a < ans:
                        ans = a
                        
        return ans

        
