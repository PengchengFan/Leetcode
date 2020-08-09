from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        ans = [[1]]

        # from 2 to numRows
        for _ in range(numRows - 1):
            newRow = [1]
            for j in range(len(ans[-1]) - 1):
                newRow.append(ans[-1][j] + ans[-1][j + 1])
            newRow.append(1)
            ans.append(newRow)
        return ans


def test():
    s = Solution()
    print(s.generate(5))


if __name__ == '__main__':
    test()
