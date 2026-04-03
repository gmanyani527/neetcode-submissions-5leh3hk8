class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1 
        last_index = n - 1

        while left <= right: 
            if abs(nums[left]) > abs(nums[right]):
                result[last_index] = nums[left] * nums[left]
                left += 1
            else: 
                result[last_index] = nums[right] * nums[right]
                right -= 1 
            last_index -= 1 
        return result 