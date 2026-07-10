class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:

            alive = True

            while stack and ast < 0 and stack[-1] > 0:

                if stack[-1] < -ast:
                    stack.pop()

                elif stack[-1] == -ast:
                    stack.pop()
                    alive = False
                    break
                
                else:
                    alive = False
                    break

            if alive:
                stack.append(ast)

        return stack
