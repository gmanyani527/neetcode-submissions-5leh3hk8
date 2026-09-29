# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        values = []
        cur = head
        while cur: 
            values.append(cur)
            cur = cur.next
        remove = len(values) - n
        if remove == 0:
            return head.next
        values[remove - 1].next = values[remove].next
        return head