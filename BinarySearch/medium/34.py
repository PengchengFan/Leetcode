from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first, last = 0, len(nums)
        while first < last:
            mid = first + (last - first) // 2
            if nums[mid] < target:
                first = mid + 1
            else:
                last = mid
        if first < len(nums) and nums[first] == target:
            startIdx = first
            last = len(nums) - 1
            while first < last:
                mid = first + (last - first) // 2
                if nums[mid] > target:
                    last = mid
                elif nums[mid + 1] > target:
                    first = mid
                    break
                else:
                    first = mid + 1
            endIdx = first
            return [startIdx, endIdx]
        else:
            return [-1, -1]


s = Solution()
assert [3, 4] == s.searchRange([5, 7, 7, 8, 8, 10], 8)
assert [-1, -1] == s.searchRange([5, 7, 7, 8, 8, 10], 6)
assert [1, 2] == s.searchRange([5, 7, 7, 8, 8, 10], 7)
assert [-1, -1] == s.searchRange([], 7)
assert [-1, -1] == s.searchRange([2, 2], 3)
assert [0, 0] == s.searchRange([1], 1)
