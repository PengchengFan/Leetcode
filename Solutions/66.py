from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = 0
            if len(digits) == 1:
                digits = [1, 0]
            else:
                digits = self.plusOne(digits[:-1])
                digits.append(0)
        return digits

s = Solution()
ans = s.plusOne([1,2,3])
print(ans)
ans = s.plusOne([4,3,2,1])
print(ans)
ans = s.plusOne([9,9,9])
print(ans)