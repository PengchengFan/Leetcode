class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.strip().split(" ")
        return len(strs[-1])

s = Solution()
ans = s.lengthOfLastWord("a ")
print(ans)