class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' 
        in - place - two pointers

        k - the variable number of unique elements

        '''

        write = 1
        k = 1

        for read in range(1,len(nums)): 
            if nums[read] == nums[read - 1]:
                continue
            else:
                nums[write] = nums[read]
                write += 1
                k += 1
        return k


