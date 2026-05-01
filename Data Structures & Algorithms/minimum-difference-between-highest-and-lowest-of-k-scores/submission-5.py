class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        diff = float("inf")
        left = 0
        right = k - 1

        while right < len(nums):
            diff = min(diff, nums[right] - nums[left])
            left += 1
            right += 1
        return diff
