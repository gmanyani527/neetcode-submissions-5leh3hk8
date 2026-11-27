# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, arr = head, [ListNode(0, head)]
        while cur:
            arr.append(cur)
            cur = cur.next
        rightMax = ListNode(0, None)
        for i  in range(len(arr) - 1, 0, -1):
            if rightMax.val > arr[i].val:
                arr[i - 1].next = rightMax
            else:
                rightMax = arr[i]
        return arr[0].next