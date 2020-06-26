from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for ind, num in enumerate(nums):
            if num in nums[ind+1:]:
                continue
            last_list = nums[:ind] + nums[ind + 1:]
            last_permutes = self.permuteUnique(last_list)
            for permute in last_permutes:
                permute = [num] + permute
                ans.append(permute)
        return ans


def test():
    s = Solution()
    assert s.permuteUnique([1, 1, 2]) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
