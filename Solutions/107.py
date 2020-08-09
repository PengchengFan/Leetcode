# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        nodes = [[0, root]]
        ans = []
        while len(nodes) > 0:
            level, node = nodes.pop(0)

            if node is not None:

                if level > len(ans) - 1:
                    ans.append([])

                ans[level].append(node.val)
                nodes.append([level + 1, node.left])
                nodes.append([level + 1, node.right])
        ans = ans[::-1]
        return ans
