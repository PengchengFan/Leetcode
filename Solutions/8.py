class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        negative = False
        if str[0] == '-':
            negative = True
            str = str[1:]
        int_str = ''
        while len(str) > 0 and str[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            int_str = int_str + str[0]
            str = str[1:]
        if negative:
            return min(int(int_str), 2**31-1)
        return max(-int(int_str[1:]), -2**31)

s = Solution()
s.myAtoi("   -42")