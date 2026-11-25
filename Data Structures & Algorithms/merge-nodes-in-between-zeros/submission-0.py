# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head.next

        while cur:
            total = 0
            while cur and cur.val != 0:
                total += cur.val
                cur = cur.next
            arr.append(total)
            if cur:
                cur = cur.next
        if not arr:
            return None
        res = ListNode(arr[0])
        cur = res
        for i in range(1,len(arr)):
            node = ListNode(arr[i])
            cur.next = node
            cur = cur.next
        return res

            