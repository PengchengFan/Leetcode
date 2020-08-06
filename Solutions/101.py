# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return (left.val == right.val) and \
                   self._isSymmetric(left.right, right.left) and \
                   self._isSymmetric(left.left, right.right)
