class Solution:
    def intToRoman(self, num: int) -> str:
        string = str(num)
        length = len(string)
        print(string, length)
        if length == 0:
            return ""
        if string[0] == '9':
            print(1, ["IX", "XC", "CM"][length - 1])
            return ["IX", "XC", "CM"][length - 1] + self.intToRoman(string[1:])
        elif string[0] == '4':
            print(2, ["IV", "XL", "CD"][length - 1])
            return ["IV", "XL", "CD"][length - 1] + self.intToRoman(string[1:])
        elif int(string[0]) < 4:
            print(3, ["I", "X", "C", "M"][length - 1] * int(string[0]))
            return ["I", "X", "C", "M"][length - 1] * int(string[0]) + self.intToRoman(string[1:])
        elif int(string[0]) < 9:
            print(4, ["V", "L", "D"][length - 1] + ["I", "X", "C", "M"][length - 1])
            return ["V", "L", "D"][length - 1] + ["I", "X", "C", "M"][length - 1] * (int(string[0]) - 5) + self.intToRoman(string[1:])

s = Solution()
print(s.intToRoman(1238))
