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

        def build(array: List, i: int, size: int) -> TreeNode:
            val = array[i]
            if val == None:
                return None
            node = TreeNode(val)
            left = 2*i + 1
            right = 2*i + 2
            if left < size:
                node.left = build(array, left, size)
            if right < size:
                node.right = build(array, right, size)
            return node
        return build(array, 0, len(array))

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
