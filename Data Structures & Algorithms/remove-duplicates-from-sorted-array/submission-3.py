class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        current = 0

        for next in range (1,len(nums)): 
            if nums[next] != nums[next - 1]:
                current += 1
                nums[current] = nums[next]
                k += 1
        return k


        