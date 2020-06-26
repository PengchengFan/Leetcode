class Solution:
    def singleNumber(self, nums) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


def test_singleNumber():
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
