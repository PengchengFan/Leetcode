from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum


def test():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
