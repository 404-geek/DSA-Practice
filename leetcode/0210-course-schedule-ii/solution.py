class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)

        status = [0] * numCourses
        ans = []

        def track(i):

            if status[i] == 1:
                return False
            if status[i] == 2:
                return True

            status[i] = 1

            for k in adj[i]:
                if not track(k):
                    return False
            
            status[i] = 2
            ans.append(i)

            return True

        for n in range(numCourses):
            
            if status[n] == 1:
                return False
            
            if status[n] == 2:
                continue
        
            if not track(n):
                return []

        return ans[::-1]





        

            
        
