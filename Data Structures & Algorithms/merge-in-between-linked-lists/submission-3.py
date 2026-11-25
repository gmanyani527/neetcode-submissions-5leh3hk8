# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = list1

        while cur: 
            arr.append(cur)
            cur = cur.next
        arr[a-1].next = list2
        cur = list2
        while cur.next:
            cur = cur.next
        cur.next = arr[b+1]
        return list1