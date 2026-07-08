
nums = [2, 3, 7, 1, 3, 5]

n = len(nums)

def merge_sort(l, r):

    if l >= r:
        return

    pivot = (l + r) // 2

    merge_sort(l, pivot)
    merge_sort(pivot + 1, r)

    merge(l, pivot, r)

def merge(l, mid, r):

    temp = []

    i = l
    j = mid + 1

    while i <= mid and j <= r:

        if nums[i] <= nums[j]:

            temp.append(nums[i])
            i+=1

        else:
            temp.append(nums[j])
            j+=1

    while i <= mid:
        temp.append(nums[i])
        i+=1

    while j <= r:
        temp.append(nums[j])
        j+=1

    for k in range(len(temp)):
        nums[l + k] = temp[k]

merge_sort(0, n-1)


print(nums)



