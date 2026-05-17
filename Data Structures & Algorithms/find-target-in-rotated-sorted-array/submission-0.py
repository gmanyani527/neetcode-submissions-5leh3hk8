class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # found target
            if nums[mid] == target:
                return mid

            # LEFT half is sorted
            if nums[left] <= nums[mid]:

                # target is inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT half is sorted
            else:

                # target is inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
