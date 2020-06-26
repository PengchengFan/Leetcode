class Solution:
    def findIntegers(self, num: int) -> int:
        cnt = 0
        for n in range(num + 1):
            binary = bin(n)
            if "11" not in binary:
                cnt += 1
        return cnt

A = Solution()
print(A.findIntegers(100000000))