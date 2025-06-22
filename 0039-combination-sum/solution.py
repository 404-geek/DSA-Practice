class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [(0, [], 0)]  # (index, current path, current sum)

        while stack:
            i, path, total = stack.pop()

            if total == target:
                res.append(path)
                continue
            if total > target:
                continue

            for j in range(i, len(candidates)):
                stack.append((j, path + [candidates[j]], total + candidates[j]))

        return res


