class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        k = 1

        for next in range(1, len(nums)):
            if nums[current] != nums[next]:
                current += 1
                nums[current] = nums[next]
                k += 1
        return k 