# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ans = True
        if p and q:
            if p.val != q.val:
                return False
            else:
                ans *= self.isSameTree(p.left, q.left)
                ans *= self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False
        return bool(ans)

def test():
    s = Solution()

if __name__ == '__main__':
    test()