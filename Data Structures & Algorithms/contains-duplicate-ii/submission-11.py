class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for i in range(len(nums)):
            if nums[i] in window: 
                return True
            else:
                window.add(nums[i])
            if i - left >= k:
                window.remove(nums[left])
                left += 1
        return False 