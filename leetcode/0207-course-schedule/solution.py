class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {}

        for a,b in prerequisites:
            if adj.get(a):
                adj[a].append(b)
            else:
                adj[a] = [b]

        state = [0] * numCourses

        def move(i):

            if state[i] == 1:
                return False
            if state[i] == 2:
                return True

            state[i] = 1

            for req in adj.get(i, []):
                if not move(req):
                    return False

            state [i] = 2
            return True
        

        for i in range(numCourses):
            if not move(i):
                return False


        return True


