# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def iterate(self, node, l):
        if node.left is not None:
            self.iterate(node.left, l)
        l.append(node.val)
        if node.right is not None:
            self.iterate(node.right, l)


    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2, ans = [], [], []
        self.iterate(root1, l1)
        self.iterate(root2, l2)
        print(l1, l2)
        while l1 or l2:
            if l1 and l2:
                if l1[0] > l2[0]:
                    ans.append(l1.pop(0))
                else:
                    ans.append(l2.pop(0))
            elif l1:
                ans.append(l1.pop(0))
            elif l2:
                ans.append(l2.pop(0))
        return ans