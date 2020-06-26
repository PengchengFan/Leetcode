class Solution:
    def sum_square(self, n):
        sum = 0
        while n >= 10:
            sum += (n % 10) ** 2
            n = n // 10
        sum += n ** 2
        return sum

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        ans = []
        while n not in ans:
            ans.append(n)
            n = self.sum_square(n)
            if n == 1:
                return True
        return False


def test():
    s = Solution()
    assert s.isHappy(19) == True
