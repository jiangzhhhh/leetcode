from typing import List, Optional
from tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l: int, r: int) -> TreeNode:
            if l == r:
                return None
            mid = (l+r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l, mid)
            node.right = build(mid+1, r)
            return node
        return build(0, len(nums))


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
