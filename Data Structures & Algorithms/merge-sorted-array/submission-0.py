class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        you must have a left and right pointer your going to 
        to start at the end of each word. remember that nums1 
        is only showing the number of valid numbers and nums2 
        shows the elements that you must add so you must keep
        track of the last element for nums1 becuase that will 
        tell you where to write the variable from nums2 in nums1
        that will be the total number of valid numbers plus the numbers
        that you have add - 1... and make sure that they are in order ofc

        """
        last = m + n - 1 
        
        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]: 
                nums1[last] = nums1[m-1]
                m -= 1
            else: 
                nums1[last] = nums2[n-1]
                n -= 1 
            last -= 1 
        while n > 0: 
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        






