class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        first_ind = 0
        second_ind = first_ind + 1
        unique_char = []
        unique_char.append(s[first_ind])
        max_len = len(unique_char)

        while second_ind < len(s):
            # print(s[first_ind], s[second_ind], first_ind, second_ind, unique_char)
            if s[second_ind] in unique_char:
                max_len = max(max_len, len(unique_char))
                first_ind = first_ind + unique_char.index(s[second_ind]) + 1
                unique_char = unique_char[unique_char.index(s[second_ind]) + 1:]
            else:
                unique_char.append(s[second_ind])
                second_ind = second_ind + 1
        # print(first_ind, second_ind, unique_char)
        max_len = max(max_len, len(unique_char))
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("au"))