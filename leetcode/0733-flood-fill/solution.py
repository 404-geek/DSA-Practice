class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        stack = [(sr, sc)]
        val = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        if val == color:
            return image

        while stack:

            r,c = stack.pop()

            if 0 <= r < rows and 0 <= c < cols and image[r][c] == val:
                image[r][c] = color

                stack.append((r+1, c))
                stack.append((r, c+1))
                stack.append((r-1,c))
                stack.append((r,c-1))

        return image

