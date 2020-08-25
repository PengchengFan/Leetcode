from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.combinationSum(candidates, 0, [], ans, target)
        return ans

    def combinationSum(self, nums, start, path, result, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]: continue
            if nums[i] > target: break
            self.combinationSum(nums, i + 1, path + [nums[i]], result, target - nums[i])


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# print(s.combinationSum2([1, 1], 1))
