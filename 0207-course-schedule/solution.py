class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = {i:[] for i in range(numCourses)} 
                
        for crse,preq in prerequisites:
            pre[crse].append(preq)
        
        finished = set() 

        def dfs(crs):

            if crs in finished:
                return False
            if pre[crs] == []:
                return True

            finished.add(crs)

            for crse in pre[crs]:
                if not dfs(crse): return False
            
            finished.remove(crs)
            pre[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        
