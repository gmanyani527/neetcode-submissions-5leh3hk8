class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1 

        while left < right:
            sum = nums[left] + nums[right]
            if sum > target: 
                right -= 1
            elif sum < target: 
                left += 1
            elif sum == target:
                return [left + 1 ,right + 1]
            else: 
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1 ]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                


        