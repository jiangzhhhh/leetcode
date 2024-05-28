from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def cmp(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            return self.cmp(p.left, q.left) and p.val == q.val and self.cmp(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.cmp(p, q)


s = Solution()
# t1 = TreeNode(1, TreeNode(2), TreeNode(3))
# t2 = TreeNode(1, TreeNode(2), TreeNode(3))
t1 = TreeNode(0, TreeNode(-5))
t2 = TreeNode(0, TreeNode(-8))
print(s.isSameTree(t1, t2))
