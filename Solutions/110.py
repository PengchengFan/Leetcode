# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.balance(root)

    def balance(self, root):
        if root is None:
            return 1

        lh = self.balance(root.left)
        rh = self.balance(root.right)

        if not lh or not rh:
            return False

        if abs(lh - rh) > 1:
            return False

        return max(lh, rh) + 1
