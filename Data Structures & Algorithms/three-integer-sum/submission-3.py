class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        first thing that we can notice from this question 
        that its asking for us to target everything to zero
        one thing that I suggest doing that I will do is sort 
        the array and this will allow for us to make sure that the
        first character that we start with or select for one of the three
        elements that equal to zero cannot be greater than zero
        cuz if it is that means the upcoming elements will all be positive...
        another thing that we must check besides that is if the character
        has been used more than once so that we cannot be selecting a duplicate
        

        next step after that would be to use the two pointer to then search 
        for the other two elements. doing that will allow for us to do the
        same that we did for two sum II because we have a sorted array 
        if that sum is eqal to that element then we are set, but if the sum is greater 
        than we decreaes the right pointer if the sum is less than we move the 
        left pointer up 1 to make the sum closer to the required amount.

        final step if the target is equal to the sum to then we must then do a final 
        step of making sure the next elements after we increment and decrement the pointers
        is that they are not duplicates

        '''
        nums = sorted(nums)
        result = []
        a = 0


        for i in range(len(nums)): 
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                target = nums[i] + nums[left] + nums[right]
                if target > 0: 
                    right -= 1
                elif target < 0: 
                    left += 1
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return result

        