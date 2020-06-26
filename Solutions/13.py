class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s[::-1]
        total = 0
        last_s = ""
        while len(s) > 0:
            curr_s = s[0]
            if last_s == "":
                total += mapping[curr_s]
            elif str(mapping[last_s]-mapping[curr_s])[0] == '4' or str(mapping[last_s]-mapping[curr_s])[0] == '9':
                total -= mapping[curr_s]
            else:
                total += mapping[curr_s]
            last_s = curr_s
            s = s[1:]

        return total

s = Solution()
print(s.romanToInt("MCMXCIV"))