# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def append(self, l3: ListNode, node: ListNode) -> (ListNode, ListNode):
        new_node = ListNode(node.val, None)
        next = node.next
        l3.next = new_node
        l3 = l3.next
        return (l3, next)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(None, None)
        l3_head = l3
        while l1 and l2:
            if l1.val <= l2.val:
                (l3, l1) = self.append(l3, l1)
            else:
                (l3, l2) = self.append(l3, l2)
        while l1:
            (l3, l1) = self.append(l3, l1)
        while l2:
            (l3, l2) = self.append(l3, l2)
        return l3_head.next


s = Solution()
l1 = ListNode(5)
l2 = ListNode(1, ListNode(2, None))
l3 = s.mergeTwoLists(l1, l2)
cur = l3
while cur:
    print(cur.val)
    cur = cur.next
