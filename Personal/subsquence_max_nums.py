def find_max_nums(k, nums):

    n = len(nums)
    max_n = 0

    def traverse(i, path):

        nonlocal max_n

        if len(path) == k:
            num = 0

            for digit in path:
                num = num * 10 + digit

            max_n = max(max_n, num)
            return
                    
        for j in range(i, n):
            
            path.append(nums[j])
            traverse(j+1, path)
            path.pop()

    traverse(0, [])

    return max_n


k = 3
nums = [1,3,2,8,9]
print(find_max_nums(k, nums))

    