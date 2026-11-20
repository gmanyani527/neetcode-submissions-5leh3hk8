# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        i,j = 0, len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            else: 
                i += 1
                j -= 1
        return True