class Solution:
    def titleToNumber(self, s: str) -> int:
        if s == '':
            return 0
        return (ord(s[-1]) - 64) + 26 * self.titleToNumber(s[:-1])

s = Solution()
assert s.titleToNumber("A") == 1
assert s.titleToNumber("AB") == 28
assert s.titleToNumber("ZY") == 701
assert s.titleToNumber("AZ") == 52