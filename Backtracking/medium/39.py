from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return
        ans = []
        for i in range(len(candidates)):
            # print(candidates)
            candidate = candidates[i]
            if target == candidate:
                ans.append([candidate])
            elif target > candidate:
                subAns = self.combinationSum(candidates[i:], target - candidate)
                for a in subAns:
                    a.append(candidate)
                    ans.append(a)
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.cs(candidates, 0, [], ans, target)
        return ans

    def cs(self, nums, start, path, result, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if target < nums[i]:
                break
            self.cs(nums, i, path + [nums[i]], result, target - nums[i])


s = Solution()
print(s.combinationSum2([2, 3, 6, 7], 7))
print(s.combinationSum2([2, 3, 5], 8))
