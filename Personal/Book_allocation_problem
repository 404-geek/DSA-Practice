class Solution:
    def findPages(self, nums, m):

        if m > len(nums):
            return -1

        su = sum(nums)
        ma = max(nums)
        
        def return_students(max_books):

            stud = 1 
            running_pages = 0

            for n in nums:

                if running_pages + n <= max_books:
                    running_pages+= n
                else:
                    stud+=1
                    running_pages = n

            return stud

        while ma <= su:

            mid = (ma + su) // 2

            if return_students(mid) <= m:
                su = mid - 1
            else:
                ma = mid + 1

        return ma



                





       