import math


class Solution:
    # simple solution
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return min(dividend // divisor, 2 ** 31 - 1)
        else:
            return max(math.ceil(dividend / divisor), - 2 ** 31 - 1)

    # binary search
    def divide2(self, dividend, divisor):
        # solution1- binary search
        ncount, flag, res = 0, 1, 0
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            flag = -1
        divisor, dividend = abs(divisor), abs(dividend)
        if divisor > dividend: return 0
        while dividend >= divisor:
            tmp = divisor
            ncount = 1
            while tmp <= dividend:
                dividend -= tmp
                res += ncount
                tmp += tmp
                ncount += ncount
        # consider the overflow, even though python3 didn't consider
        if res * flag < -2147483648:
            return -2147483648
        elif res * flag > 2147483647:
            return 2147483647
        else:
            return res * flag
