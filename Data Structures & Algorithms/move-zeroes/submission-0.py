class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0

        for next in range(len(nums)):
            if nums[next] != 0: 
                nums[current] = nums[next]
                current += 1
        while current < len(nums): 
            nums[current] = 0
            current += 1
        return nums