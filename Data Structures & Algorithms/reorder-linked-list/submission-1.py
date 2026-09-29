# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        values = []

        while head:
            values.append(head)
            head = head.next
        i, j = 0, len(values) - 1
        while i < j: 
            values[i].next = values[j]
            i+=1
            if i >=j: 
                break
            values[j].next = values[i]
            j-=1
        values[i].next = None
            
