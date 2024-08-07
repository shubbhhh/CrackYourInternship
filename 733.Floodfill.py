class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        toColor = image[sr][sc]
        queue = deque([ (sr, sc) ])
        seen = set()
        rows, cols = len(image), len(image[0])

        while queue:
            row, col = queue.popleft()
            if (0 <= row < rows 
                and 0 <= col < cols 
                and (row, col) not in seen 
                and image[row][col] == toColor):

                image[row][col] = color
                seen.add((row, col))
                for (nr, nc) in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    queue.append((nr, nc))

        return image