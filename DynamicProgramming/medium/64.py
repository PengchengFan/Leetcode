from typing import List


class Solution:
    # bottom up
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                # print("-----------", i, j)
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    # print(grid[i][j], "+", grid[i][j - 1])
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                    continue
                if j == 0:
                    # print(grid[i][j], "+", grid[i - 1][j])
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                    continue
                # print(grid[i - 1][j], "+", min(grid[i - 1][j], grid[i][j - 1]))
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
                # print(grid)
        return grid[m - 1][n - 1]


s = Solution()
g = [
    [1],
]
print(s.minPathSum(g))
