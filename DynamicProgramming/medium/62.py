class Solution:

    # recursive: TLE
    def uniquePaths_recursive(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if n == 1:
            return 1
        return self.uniquePaths_recursive(m - 1, n) + self.uniquePaths_recursive(m, n - 1)

    # with memo
    def uniquePaths_memo(self, m: int, n: int) -> int:
        memo = [[1] * (n + 1) for _ in range(m + 1)]

        def _uniquePaths(m, n, me):
            if m != 1 and n != 1 and me[m][n] == 1:
                ans = _uniquePaths(m - 1, n, me) + _uniquePaths(m, n - 1, me)
                me[m][n] = ans
            return me[m][n]

        return _uniquePaths(m, n, memo)

    # bottom-up
    def uniquePaths_bottom_up(self, m: int, n: int) -> int:
        memo = [[1] * (n + 1) for _ in range(m + 1)]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m][n]

    # math: Total permutations = (m+n)! / (m! * n!)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        m -= 1
        n -= 1
        ans = 1
        for i in range(n):
            ans *= (m + i + 1)
            ans /= i + 1
        return int(ans)


s = Solution()
print(s.uniquePaths(3, 2))
