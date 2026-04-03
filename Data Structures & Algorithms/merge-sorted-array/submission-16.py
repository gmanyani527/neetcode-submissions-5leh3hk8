class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        we are given an array and we are given the number of valid
        elements that we have and another array with an int telling
        us the number of values that will be added. we know that 
        m + n is the total length and to be able to start from the back 
        we can do last = m + n - 1 and then traverse comparing both and
        merging

        '''
        last = m+n-1

        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else: 
                nums1[last] = nums2[n-1]
                n-=1 
            last -= 1
        while n > 0: 
            nums1[last] = nums2[n-1]
            n -=1
            last -= 1 