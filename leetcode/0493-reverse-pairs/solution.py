class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        cnt = 0
        n = len(nums)

        def find_pairs(a, b):
            cnt = 0
            last_ind = 0
            j = 0
            for n in a:
                while j < len(b) and n > 2 * b[j]:
                    j+=1
                cnt+=j
            return cnt

        def merge(l, r):
            nonlocal cnt

            if l == r:
                return [nums[l]]

            mid = (l + r) // 2

            a = merge(l, mid)
            b = merge(mid + 1, r)

            cnt += find_pairs(a, b)

            temp = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    temp.append(a[i])
                    i += 1
                else:
                    temp.append(b[j])
                    j += 1

            temp.extend(a[i:])
            temp.extend(b[j:])

            return temp

        if not nums:
            return 0

        merge(0, n - 1)
        return cnt
