from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums]
        for ind, num in enumerate(nums):
            last_list = nums[:ind] + nums[ind + 1:]
            last_permutes = self.permute(last_list)
            for permute in last_permutes:
                permute = [num] + permute
                ans.append(permute)
        return ans


def test():
    s = Solution()
    assert s.permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
