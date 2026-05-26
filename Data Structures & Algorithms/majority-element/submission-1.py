class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        answer = 0
        maxCount = 0

        for num in nums: 
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1
                
            if count[num] >  maxCount:
                maxCount = count[num]
                result = num
        return result