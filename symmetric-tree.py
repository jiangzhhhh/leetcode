from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, left: TreeNode, right: TreeNode):
        if left == right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root)
