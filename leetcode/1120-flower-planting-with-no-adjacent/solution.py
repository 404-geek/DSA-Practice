class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        node_s = [0] * (n+1)
        map = defaultdict(list)

        for a, b in paths:

            map[a].append(b)
            map[b].append(a)

        def safe(node, k):
            for nei in map[node]:
                if node_s[nei] == k:
                    return False
            return True

        for node in range(1, n+1):

            for i in range(1,5):
                if not safe(node, i):
                    continue
                node_s[node] = i
                break

        return node_s[1:]
