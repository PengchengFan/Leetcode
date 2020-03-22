class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last_str = ""
        curr_str = ""
        if (len(strs) == 0):
            return last_str
        for i in range(len(strs[0]) + 1):
            curr_str = strs[0][:i]
            for string in strs:
                if curr_str != string[:i]:
                    return last_str
            last_str = curr_str
        return last_str

s = Solution()
print(s.longestCommonPrefix(["a"]))