class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        last_index = len(nums) - 1

        while left <= right: 
            if abs(nums[left]) > abs(nums[right]):
                result[last_index] = nums[left] * nums[left]
                left += 1
            else: 
                result[last_index] = nums[right] * nums[right]
                right -= 1 
            last_index -= 1
        return result