# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = [] 
        cur = head

        while cur: 
            arr.append(cur)
            cur = cur.next
        remove = len(arr) - n
        if remove == 0:
            return head.next
        arr[remove - 1].next = arr[remove].next
        return head
