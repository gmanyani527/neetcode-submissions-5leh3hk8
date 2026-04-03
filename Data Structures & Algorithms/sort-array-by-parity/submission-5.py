class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 0: 
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
        return nums