import math


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.trunc(math.sqrt(x))


def test():
    s = Solution()
    assert 2 == s.mySqrt(4)
    assert 2 == s.mySqrt(8)


if __name__ == '__main__':
    test()
