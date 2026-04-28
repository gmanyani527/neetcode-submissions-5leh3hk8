class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #we need to find how many students it will take to find the minimum possble difference

        nums.sort()

        left = 0
        right = k - 1
        minF = float('inf')

        while right < len(nums): 
            minF = min(minF, nums[right] - nums[left])
            left += 1
            right += 1
        return minF
