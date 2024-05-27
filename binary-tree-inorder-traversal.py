# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def walk(self, node: TreeNode, result: List[int]):
        if not node:
            return result
        if node.left:
            self.walk(node.left, result)
        result.append(node.val)
        if node.right:
            self.walk(node.right, result)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.walk(root, [])


s = Solution()
t = TreeNode(1, None, TreeNode(2, TreeNode(3, None), None))
print(s.inorderTraversal(t))
