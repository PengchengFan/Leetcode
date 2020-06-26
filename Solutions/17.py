class Solution:
    def letterCombinations(self, digits: str):
        arr = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        while len(digits) > 0:
            curr_int = int(digits[0])
            digits = digits[1:]
            if len(result) == 0:
                for char in arr[curr_int]:
                    result.append(char)
            else:
                new_result = []
                for string in result:
                    for char in arr[curr_int]:
                        new_result.append(string + char)
                result = new_result
        return result

s = Solution()
print(s.letterCombinations(""))