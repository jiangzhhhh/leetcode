from typing import Optional
from tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: TreeNode) -> int:
            if node == None:
                return 0
            else:
                return 1 + max(depth(node.left), depth(node.right))

        if not root:
            return True
        diff = depth(root.left) - depth(root.right)
        return abs(diff) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


s = Solution()
# t = TreeNode.from_array([3, 9, 20, None, None, 15, 7])
# print(s.isBalanced(t))
t = TreeNode.from_array([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
print(s.isBalanced(t))
