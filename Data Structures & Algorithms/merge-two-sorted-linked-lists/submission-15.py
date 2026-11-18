# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = [] 
        
        while list1 and list2: 
            if list1.val < list2.val: 
                arr.append(list1.val)
                list1 = list1.next
            else: 
                arr.append(list2.val)
                list2 = list2.next
        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next
        if not arr:
            return None
        res = ListNode(arr[0])
        cur = res
        for i in range(1, len(arr)):
            node = ListNode(arr[i])
            cur.next = node
            cur = cur.next
        return res
        