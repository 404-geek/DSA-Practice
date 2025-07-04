class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        stack = [(sr,sc)]
        original_color = image[sr][sc]

        if original_color ==color:
            return image
            
        m = len(image)
        n = len(image[0])

        while stack:
            r, c = stack.pop()
            
            if not (0 <= r < m and 0 <= c < n):
                continue  # skip out-of-bounds

            if image[r][c] != original_color:
                continue  # not part of the region

            image[r][c] = color

            # Push neighbors
            stack.append((r+1, c))
            stack.append((r-1, c))
            stack.append((r, c+1))
            stack.append((r, c-1))

        return image



        
        
