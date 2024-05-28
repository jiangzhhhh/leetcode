from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(array) -> 'TreeNode':
        if not array:
            return None

        def build(node: TreeNode, array: List, i: int, size: int):
            node.val = array[i]
            left = 2*i + 1
            right = 2*i + 2
            if left < size:
                node.left = TreeNode()
                build(node.left, array, left, size)
            if right < size:
                node.right = TreeNode()
                build(node.right, array, right, size)
        root = TreeNode()
        build(root, array, 0, len(array))
        return root

    def __str__(self) -> str:
        def walk(node: TreeNode):
            s = f'{node.val}'
            if node.left:
                s += f',{walk(node.left)}'
            if node.right:
                s += f',{walk(node.right)}'
            return s
        return f'[{walk(self)}]'


if __name__ == '__main__':
    t = TreeNode.from_array([3, 9, 20, None, None, 15, 7])
    print(t)
