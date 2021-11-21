class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited: List[List[bool]] = [[]] * len(grid)
        count = 0
        for index, val in enumerate(grid):
            visited[index] = [False] * len(val)

        for index_i, val in enumerate(grid):
            for index_j, cell in enumerate(val):
                if cell == '1' and not visited[index_i][index_j]:
                    count += 1
                    self.traverse(grid, visited, index_i, index_j)

        return count

    def traverse(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        elif visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = True
        self.traverse(grid, visited, i - 1, j)
        self.traverse(grid, visited, i + 1, j)
        self.traverse(grid, visited, i, j - 1)
        self.traverse(grid, visited, i, j + 1)
