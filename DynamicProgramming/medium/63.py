from typing import List


class Solution:
    # recursive with memo
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1: return 0

        # default -1 cuz there is not always a solution
        memo = [[-1] * n for _ in range(m)]

        def _uniquePaths(m, n, me):
            if m == 0 and n == 0:
                if obstacleGrid[0][0] == 0:
                    return 1
                else:
                    return 0
            if me[m][n] == -1:
                ans = 0
                if m > 0 and obstacleGrid[m - 1][n] == 0:
                    ans += _uniquePaths(m - 1, n, me)
                if n > 0 and obstacleGrid[m][n - 1] == 0:
                    ans += _uniquePaths(m, n - 1, me)
                me[m][n] = ans
            return me[m][n]

        return _uniquePaths(m - 1, n - 1, memo)




s = Solution()
ob = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
ob1 = [[1]]
ob2 = [[1, 0]]
print(s.uniquePathsWithObstacles(ob2))
