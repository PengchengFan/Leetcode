class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        solution = []
        ind = 0
        while ind < len(nums) - 3:
            elem = nums[ind]
            results = self.threeSum(nums[ind + 1:], target - elem)
            if len(results) > 0:
                for result in results:
                    result.append(elem)
                    for sol in solution:
                        if set(sol) == set(result):
                            break
                    else:
                        solution.append(result)
            ind += 1
        return solution
    def threeSum(self, nums, target):
        solution = []
        ind = 0
        while ind < len(nums) - 2:
            elem = nums[ind]
            results = self.twoSum(nums[ind + 1:], target - elem)
            if len(results) > 0:
                for result in results:
                    result.append(elem)
            solution.extend(results)
            ind += 1
        return solution
    def twoSum(self, nums, target):
        results = []
        
        ind1, ind2 = 0, len(nums) - 1
        while ind1 < ind2:
            if nums[ind1] + nums[ind2] < target:
                ind1 += 1
            elif nums[ind1] + nums[ind2] > target:
                ind2 -= 1
            else:
                for result in results:
                    if set([nums[ind1], nums[ind2]]) == set(result):
                        break
                else:
                    results.append([nums[ind1], nums[ind2]])
                ind1 += 1
        return results

s = Solution()
print(s.fourSum([-3,-2,-1,0,0,1,2,3], 0))