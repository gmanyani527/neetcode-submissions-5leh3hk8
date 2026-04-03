class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        we are given two arrays and they are are in sorted order
        which means that two pointers looks like the correct choice
        here because we all be comparing the values in each iteration 
        to choose whichever element that will be placed at the end
        largest will always go to the end right and if nums1 has the 
        larger elements then we will fill im the beginnging of the 
        nums1 elements with the elements in nums2

        """
        last = m+n-1

        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1 
            else: 
                nums1[last] = nums2[n-1]
                n-= 1
            last -= 1
        while n > 0: 
            nums1[last] = nums2[n-1]
            n-=1
            last-= 1
        
