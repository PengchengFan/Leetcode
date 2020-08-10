class Solution:
    def convertToTitle(self, n: int) -> str:
        n -= 1
        if n < 26:
            return chr(65 + n)
        else:
            return self.convertToTitle(n // 26) + chr(n % 26 + 65)

s = Solution()
assert s.convertToTitle(28) == 'AB'
assert s.convertToTitle(701) == 'ZY'
print(s.convertToTitle(52))