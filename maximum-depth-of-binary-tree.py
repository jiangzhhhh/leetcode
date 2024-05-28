from typing import Optional
from tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def walk(node: TreeNode) -> int:
            if not node:
                return 0
            else:
                depth = 1
                left = 0
                right = 0
                if node.left:
                    left = walk(node.left)
                if node.right:
                    right = walk(node.right)
                depth += max(left, right)
                return depth
        return walk(root)


s = Solution()
# print(s.maxDepth(TreeNode.from_array([3, 9, 20, None, None, 15, 7])))  # 3
print(s.maxDepth(TreeNode.from_array([1, None, 2])))  # 2
