class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:

        adj = defaultdict(list)

        n = len(nums)

        for e in edges:
            e1, e2 = e
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(node, parent, target):

            nonlocal cnt

            su = nums[node]

            for chld in adj[node]:

                if chld == parent:
                    continue

                su += dfs(chld, node, target)

            if su == target:
                cnt += 1
                return 0

            return su

        total = sum(nums)

        for comp in range(n,1,-1):

            if total % comp != 0:
                continue

            cnt = 0
            target = total // comp

            dfs(0, None, target)

            if cnt == comp:
                return comp - 1

        return 0
