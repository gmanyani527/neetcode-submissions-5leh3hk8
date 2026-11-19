# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head 

        while cur: 
            arr.append(cur)
            cur = cur.next
        
        start, end = 0, len(arr) - 1
        while start < end: 
            arr[start].next = arr[end]
            start += 1
            if start >= end: 
                break
            arr[end].next = arr[start]
            end-=1
        arr[start].next = None

