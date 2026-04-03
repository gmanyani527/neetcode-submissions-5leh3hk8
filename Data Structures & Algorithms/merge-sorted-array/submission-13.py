class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length1, length2 = len(nums1), len(nums2)
        a, b = 0, 0
        last = m+n-1

        while 0 < m and 0 < n: 
            if nums1[m - 1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else: 
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        while 0 < n: 
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1