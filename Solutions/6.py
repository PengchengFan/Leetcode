class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        s = s + " " * ((numRows * 2 - 2) - len(s) % (numRows * 2 - 2))
        for i in range(numRows - 1, -1, -1):
            offset = numRows - i - 1
            substr, ind = "", numRows - 1
            while ind < len(s):
                if offset == 0 or offset == numRows - 1:
                    substr += s[ind - offset]
                else:
                    substr += s[ind - offset]
                    substr += s[ind + offset]
                ind += (2 * numRows) - 2
            ans = substr + ans
        return ans.replace(" ", "")


def test():
    s = Solution()
    assert 'PINALSIGYAHRPI' == s.convert('PAYPALISHIRING', 4)
    assert 'PAHNAPLSIIGYIR' == s.convert('PAYPALISHIRING', 3)


if '__main__' == __name__:
    test()
