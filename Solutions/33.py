from typing import List


class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:
                # at larger sublist
                if nums[mid] <= target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # at smaller sublist
                if nums[mid] >= target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    def mysearch(self, nums: List[int], target: int) -> int:
        ind = -1
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) // 2
            if target == nums[mid]:
                ind = mid
                break
            if nums[mid] > nums[left]:
                # at larger sublist
                if nums[mid] > target > nums[left]:
                    right = mid
                else:
                    left = mid
            if nums[mid] < nums[left]:
                # at smaller sublist
                if nums[mid] < target < nums[right]:
                    left = mid
                else:
                    right = mid
        return ind


def test():
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([5, 1, 3], 5) == 0
