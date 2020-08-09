# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.tree(0, len(nums) - 1, nums)

    def tree(self, low, high, nums):
        while low <= high:
            node = TreeNode()
            mid = (low + high) // 2
            node.val = nums[mid]
            node.left = self.tree(low, mid - 1, nums)
            node.right = self.tree(mid + 1, high, nums)
            return node
