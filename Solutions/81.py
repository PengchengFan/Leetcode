class Solution:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
                continue
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
        return False

    def right_search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
                continue
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
        return False


def test():
    s = Solution()
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) == True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) == False
    assert s.search([1, 3, 1, 1, 1], 3) == True
    assert s.search([3, 1], 1) == True
