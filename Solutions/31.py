class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_ind = len(nums) - 1
        while current_ind > 0:
            next_ind = current_ind - 1
            if nums[current_ind] > nums[next_ind]:
                nums[current_ind:] = nums[current_ind:][::-1]
                for ind, num in enumerate(nums[current_ind:]):
                    print(nums)
                    if num > nums[next_ind]:
                        nums[next_ind], nums[current_ind + ind] = nums[current_ind + ind], nums[next_ind]
                        break
                return
            if nums[current_ind] <= nums[next_ind]:
                current_ind -= 1
                continue
            current_ind -= 1
        nums.sort()


def test_nextPermutation():
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    assert nums == [1, 3, 2]
    s.nextPermutation(nums)
    assert nums == [2, 1, 3]
    s.nextPermutation(nums)
    assert nums == [2, 3, 1]
