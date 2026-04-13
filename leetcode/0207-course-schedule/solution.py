class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for a, b in prerequisites:

            adj[b].append(a)

        status = [0] * numCourses

        def traverse(a):

            if status[a] == 1:
                return False

            if status[a] == 2:
                return True

            status[a] = 1

            for n in adj[a]:
                if not traverse(n):
                    return False
            
            status[a] = 2
            return True
            
        for i in range(numCourses):
            if not traverse(i):
                return False

        return True




