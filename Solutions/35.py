from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
ans = s.searchInsert([1,3,5,6], 5)
print(ans)
ans = s.searchInsert([1,3,5,6], 2)
print(ans)
ans = s.searchInsert([1,3,5,6], 7)
print(ans)
ans = s.searchInsert([1,3,5,6], 0)
print(ans)
