class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for ind, char in enumerate(haystack):
            if haystack[ind:ind+len(needle)] == needle:
                return ind
        return -1

s = Solution()
print(s.strStr("hello", "ll"))