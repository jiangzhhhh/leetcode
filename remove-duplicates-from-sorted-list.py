# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            next = cur.next
            while next and cur.val == next.val:
                next = next.next
            cur.next = next
            cur = next
        return head


s = Solution()
# [1,1]
list = ListNode(1, ListNode(1))
result = s.deleteDuplicates(list)
cur = result
while cur:
    print(cur.val)
    cur = cur.next
